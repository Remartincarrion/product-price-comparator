import pandas as pd
import utils as ut


def load_data(file_path):
    try:
        df = pd.read_csv(file_path) # Read csv with pandas
        return df
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def save_report(data, external_data):
    with open("report.md", "w") as f:
        f.write("# Insights Report\n")
        f.write("This report compare prices between the small business products and products data from an important supermarket used as reference. \n\n")
        
        # Iterate in our own dataset
        for index, row in data.iterrows():
            product_name = row['product_name']
            our_price = row["our_price"] 

            # Support for prices which include '$'
            if isinstance(our_price, str):
                our_price = float(our_price.replace("$", "").strip()) 
            

            # Find the most similar product in the external dataset
            best_match = None
            best_similarity = 0

            for item in external_data: 
                similarity = ut.similarity(product_name.lower(), item['name'].lower())
                if similarity > best_similarity: 
                    best_similarity = similarity
                    best_match = item

            # Compare prices if there is a good enough match (at least 80%)
            if best_match and best_similarity >= 0.8:
                external_price = best_match['price']

                if our_price < external_price:
                    comparison = "below"
                elif our_price > external_price:
                    comparison = "above"
                else:
                    comparison = "equal"

                f.write(f"- **{product_name}** is **{comparison}** the reference price ({external_price} USD) with a diference of {our_price - external_price} USD.\n")
                f.write(f"  - Mini market price: {our_price} USD\n")
                f.write(f"  - Reference product: {best_match['name']} (Similarity: {best_similarity:.2f})\n\n")
        






if __name__ == "__main__":
    file_path = "data/products.csv"  
    data = load_data(file_path)

    external_data = ut.fetch_external_data()

    if external_data:
        save_report(data, external_data)
        print("Insights Report generated succesfully")
    else: 
        print("Error: No external data found")













