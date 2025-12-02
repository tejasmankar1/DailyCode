def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} Chai.....")
        if flavor == "unknown":
            raise ValueError("we dont know this flavor")
    except ValueError as e:
        print("Error :",e)
    else:
        print(f"Serving {flavor} chai...")
    finally:
        print("next customer please")

serve_chai("masala")
serve_chai("unknown")