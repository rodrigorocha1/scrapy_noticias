for noticia in response.css('p.bullet'):
    texto = noticia.css('::text').getall
    if "Reuters" in texto or "Por " in texto:  # Filtra parágrafos indesejados
        continue

    print("".join(texto).strip())
    print()
