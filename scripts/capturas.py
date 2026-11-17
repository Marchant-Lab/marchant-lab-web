"""Genera el sitio y toma capturas de cada página (escritorio y celular) para revisar el diseño.

Uso (desde la raíz, entorno conda marchant-lab-web): python scripts/capturas.py [carpeta_salida]
"""
import functools, http.server, subprocess, sys, tempfile, threading
from pathlib import Path
from playwright.sync_api import sync_playwright

salida = Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp/capturas")
salida.mkdir(parents=True, exist_ok=True)
sitio = Path(tempfile.mkdtemp()) / "sitio"
subprocess.run(["jekyll", "build", "-q", "--baseurl", "", "-d", str(sitio)], check=True)

manejador = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(sitio))
servidor = http.server.ThreadingHTTPServer(("127.0.0.1", 0), manejador)
threading.Thread(target=servidor.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{servidor.server_port}"

paginas = ["", "investigador/", "proyectos/", "publicaciones/", "docencia/", "equipo/", "vinculate/"]
with sync_playwright() as p:
    nav = p.chromium.launch()
    for nombre, vista in [("escritorio", {"width": 1280, "height": 900}), ("celular", {"width": 390, "height": 844})]:
        pag = nav.new_page(viewport=vista)
        for ruta in paginas:
            pag.goto(base + "/" + ruta, wait_until="networkidle")
            archivo = salida / f"{nombre}_{(ruta.strip('/') or 'inicio')}.png"
            pag.screenshot(path=str(archivo), full_page=True)
            print(archivo)
    nav.close()
servidor.shutdown()
