import src.settings as settings
from src.lastFiveyears import read_csv, serie_lastFiveyears, save_csv

input_cvs = settings.BASE_DIR / "data" / "California_Wildfire_Damage.csv"
output_cvs = settings.BASE_DIR / "data" / "output.cvs"
df = read_csv(input_cvs)
df = serie_lastFiveyears(df, "Date")
save_csv(output_cvs, df)

