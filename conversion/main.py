import src.settings as settings
from src.conversion import read_csv, serie_conversion, save_csv

input_cvs = settings.BASE_DIR / "data" / "California_Wildfire_Damage.csv"
output_cvs = settings.BASE_DIR / "data" / "output.cvs"
df = read_csv(input_cvs)
df = serie_conversion(df, "Area_Burned (Acres)")
save_csv(output_cvs, df)

