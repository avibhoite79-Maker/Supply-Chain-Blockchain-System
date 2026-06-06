from blockchain import Blockchain
import database
database.create_table()
bc=Blockchain()
while True:
    print("\nSupply Chain Tracking System")
    print("1. Add Product Stage")
    print("2. View Blockchain")
    print("3. Exit")
    choice=input("Enter Choice: ")
    if choice=="1":
        pid=input("Product ID: ")
        stage=input("Stage: ")
        owner=input("Owner: ")
        location=input("Location: ")
        data={
            "Product":pid,
            "Stage":stage,
            "Owner":owner,
            "Location":location
        }
        bc.add_block(data)
        latest=bc.chain[-1]
        database.insert_data(
            pid,
            stage,
            owner,
            location,
            latest.hash
        )
        print("Product stage added to blockchain")
    elif choice=="2":
        print("\nBlockchain Records:")
        for block in bc.chain:
            print("Index:", block.index)
            print("Data:", block.data)
            print("Hash:", block.hash)
            print("---------------------")

    elif choice=="3":
        break
