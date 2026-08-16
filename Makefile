sync:
	@echo "[*] Initializing automated state synchronization..."
	git add .
	git commit -m "auto-sync: state inventory update $(shell date -u +'%Y-%m-%d %H:%M:%S UTC')" || echo "[+] No changes to commit."
	git push origin main || echo "[!] Remote sync skipped or unconfigured."
	@echo "[+] Synchronization pipeline complete."
