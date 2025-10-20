import hashlib
import os
import sys

print("Algorithms available: MD5 | SHA1 | SHA224 | SHA256 | SHA384 | SHA512")

hash_type = input("what is the hash type?: ").strip().upper()
wordlist_location = input("Enter the wordlist location: ").strip()
target_hash = input("Enter the hash: ").strip().lower()

if not os.path.isfile(wordlist_location):
    print(f"Wordlist file not found: {wordlist_location}")
    sys.exit(1)

valid = {
    "MD5": hashlib.md5,
    "SHA1": hashlib.sha1,
    "SHA224": hashlib.sha224,
    "SHA256": hashlib.sha256,
    "SHA384": hashlib.sha384,
    "SHA512": hashlib.sha512,
}

if hash_type not in valid:
    print("Choose only the given options of hash type:", ", ".join(sorted(valid.keys())))
    sys.exit(1)

hash_func = valid[hash_type]

found = False
try:
    with open(wordlist_location, "rb") as fh:
        for lineno, line in enumerate(fh, start=1):
            candidate_bytes = line.rstrip(b"\r\n")     
            if not candidate_bytes:
                continue
            hexd = hash_func(candidate_bytes).hexdigest().lower()
            if hexd == target_hash:
                try:
                    candidate_display = candidate_bytes.decode("utf-8")
                except Exception:
                    candidate_display = repr(candidate_bytes)
                print(f"\033[1;32mHASH FOUND: {candidate_display}\033[0m  (line {lineno})")
                found = True
                break
except Exception as e:
    print("Error while reading/processing the wordlist:", e)
    sys.exit(1)

if not found:
    print("Hash not found in wordlist.")