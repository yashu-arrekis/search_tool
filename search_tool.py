query = input("Enter your query: ").strip()

def search_tool(query):
    if isinstance(query, str):
        pass
    elif query is None:
        return "query cant be None"
    else:
        return "query isnt a string"
    if not query.strip():
        return "query can't be just spaces or empty."

    try:
        chk = float(query)
        return "query cant be an integer or float or negative integer."
    except ValueError:
        pass

    return query

print(search_tool(query))