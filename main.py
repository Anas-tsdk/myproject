from src.utils.get_data import get_data
from src.utils.clean_data import clean_data

if __name__ == "__main__":
	data = get_data()   
	clean_data(data)