import argparse, json, csv, requests
from datetime import datetime
from strategies.sequential import sequential_ids
from strategies.encoded import encoded_ids

ENDPOINTS = [
    {"path": "/api/users/{id}",  "method": "GET", "label": "User Profile"},
    {"path": "/api/orders/{id}", "method": "GET", "label": "Orders"},
    {"path": "/api/docs/{id}",   "method": "GET", "label": "Documents"},
]

CALLER_HEADERS = {"X-User-ID": "1"}
OWNED_IDS = {1}

def test_endpoint(base_url, endpoint, test_ids):
    findings = []
    for obj_id in test_ids:
        url = base_url + endpoint["path"].format(id=obj_id)
        try:
            resp = requests.request(endpoint["method"], url, headers=CALLER_HEADERS, timeout=5)
            is_vuln = resp.status_code == 200 and obj_id not in OWNED_IDS
            findings.append({
                "endpoint": endpoint["label"],
                "url": url,
                "id_tested": obj_id,
                "status_code": resp.status_code,
                "response_size": len(resp.content),
                "is_idor": is_vuln,
                "timestamp": datetime.utcnow().isoformat()
            })
            flag = "🚨 IDOR" if is_vuln else "  OK  "
            print(f"[{flag}] {url} → {resp.status_code}")
        except requests.RequestException as e:
            print(f"[ERROR] {url} → {e}")
    return findings

def save_results(findings):
    with open("results/fuzzer_results.json", "w") as f:
        json.dump(findings, f, indent=2)
    with open("results/fuzzer_results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=findings[0].keys())
        writer.writeheader()
        writer.writerows(findings)
    print(f"\n✅ Results saved to fuzzer/results/")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target",   default="http://localhost:5001")
    parser.add_argument("--strategy", choices=["sequential", "encoded"], default="sequential")
    parser.add_argument("--start",    type=int, default=1)
    parser.add_argument("--end",      type=int, default=15)
    args = parser.parse_args()

    print(f"\n🔍 IDOR Fuzzer | Target: {args.target} | Strategy: {args.strategy}")
    print("=" * 60)

    test_ids = sequential_ids(args.start, args.end) if args.strategy == "sequential" else encoded_ids(args.start, args.end)

    all_findings = []
    for ep in ENDPOINTS:
        print(f"\n[*] Testing: {ep['label']}")
        all_findings.extend(test_endpoint(args.target, ep, test_ids))

    vuln_count = sum(1 for f in all_findings if f["is_idor"])
    print(f"\n{'='*60}")
    print(f"📊 Total tested : {len(all_findings)}")
    print(f"🚨 IDOR findings: {vuln_count}")
    print(f"{'='*60}\n")
    save_results(all_findings)

if __name__ == "__main__":
    main()
