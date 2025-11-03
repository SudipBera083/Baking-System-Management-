import os
from contextlib import contextmanager
import oracledb

# conn.py
# Minimal Oracle DB connection helper using python-oracledb (oracledb)
# Install with: pip install oracledb


# Configuration via environment variables (preferred)
# ORACLE_USER, ORACLE_PASSWORD, ORACLE_HOST, ORACLE_PORT, ORACLE_SERVICE or ORACLE_DSN
USER = os.getenv("ORACLE_USER")
PASSWORD = os.getenv("ORACLE_PASSWORD")
HOST = os.getenv("ORACLE_HOST", "localhost")
PORT = os.getenv("ORACLE_PORT", "1521")
SERVICE = os.getenv("ORACLE_SERVICE", "ORCLPDB1")
DSN = os.getenv("ORACLE_DSN") or f"{HOST}:{PORT}/{SERVICE}"

_pool = None

def _ensure_credentials():
    if not USER or not PASSWORD:
        raise RuntimeError("Missing Oracle credentials. Set ORACLE_USER and ORACLE_PASSWORD env vars.")

def init_pool(min=1, max=5, increment=1):
    """
    Initialize a connection pool. Call once at app startup.
    Returns the created pool.
    """
    global _pool
    if _pool:
        return _pool
    _ensure_credentials()
    _pool = oracledb.create_pool(user=USER, password=PASSWORD, dsn=DSN,
                                 min=min, max=max, increment=increment)
    return _pool

def get_connection():
    """
    Acquire a connection from the pool if initialized, otherwise open a standalone connection.
    Caller must close the connection when done (or use the `connection()` context manager).
    """
    _ensure_credentials()
    if _pool:
        return _pool.acquire()
    return oracledb.connect(user=USER, password=PASSWORD, dsn=DSN)

@contextmanager
def connection():
    """
    Context manager that yields a connection and ensures it is closed/released.
    Usage:
        with connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT 1 FROM DUAL")
            ...
    """
    conn = None
    try:
        conn = get_connection()
        yield conn
    finally:
        if conn:
            try:
                # If connection was acquired from a pool, close() releases it to the pool.
                conn.close()
            except Exception:
                pass

# Example usage when run directly (use env vars before running)
if __name__ == "__main__":
    try:
        init_pool()  # optional; without it, get_connection() opens a direct connection
    except RuntimeError as e:
        print("ERROR:", e)
        raise

    with connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT sysdate FROM dual")
        print("DB time:", cur.fetchone()[0])
        cur.close()