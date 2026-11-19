import urllib.request

def get_html(url):
    req=urllib.request.urlopen(url)
    html=req.read().decode("utf-8")
    return html


if __name__ == "__main__":
    url="http://bienestar.unsaac.edu.pe/"

    f=open("pagina.html","w",encoding="utf-8")
    f.write(get_html(url))
    f.close()
    print("Finalizado")
