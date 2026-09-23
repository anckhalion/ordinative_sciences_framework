"""Create an unfilled, hash-bound review request; never fabricate a review."""
import argparse
import json
from pathlib import Path
from validate_lexx_output import load_json, sha256_bytes


def review_template(source, output):
    data = load_json(output)
    return {
        "source_sha256": sha256_bytes(Path(source).read_bytes()),
        "output_sha256": sha256_bytes(Path(output).read_bytes()),
        "reviewer_id": "", "review_run_id": "", "independent_declared": False,
        "items": [{"flaw_id": flaw["id"],
                   "proposal_sha256": sha256_bytes(flaw["controproposta"]["forma_equa"].encode("utf-8")),
                   "independent_restrip": {"iota_primo": "", "payload_primo": []},
                   "invariant_preserved": None, "lambda_post": "vuoto", "reason": ""}
                  for flaw in data["falle"] if flaw["controproposta"]["status"] == "proposed"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--review", required=True, type=Path)
    args = parser.parse_args()
    result = review_template(args.source, args.output)
    with args.review.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
