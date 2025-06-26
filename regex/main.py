import src.settings as settings
from src.substitution import read_csv, serie_substitute, save_csv

input_cvs = settings.BASE_DIR / "data" / "California_Wildfire_Damage.csv"
output_cvs = settings.BASE_DIR / "data" / "output.cvs"
df = read_csv(input_cvs)
df = serie_substitute(df, "Location")
save_csv(output_cvs, df)