a = input("Enter the file name with extension like (.pdf,.doc) :")

if a.endswith(".pdf") or a.endswith(".doc"):
    print("Your file uploaded successfully...")
else:
    print("Please write the valid file name...")    