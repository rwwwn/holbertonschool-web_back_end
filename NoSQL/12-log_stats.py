#!/usr/bin/env python3
"""Provide stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def main() -> None:
    """Print stats in the exact format required by the project."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    total = collection.count_documents({})
    print(f"{total} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        count = collection.count_documents({"method": m})
        print(f"\tmethod {m}: {count}")

    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_count} status check")


if __name__ == "__main__":
    main()
