import pandas as pd

"""
# rename column names in pandas
df = df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'})
"""

df = pd.DataFrame([['John', 'Science', 'Pass'], ['Johnny', 'Maths', 'Pass'], ['Janardhan', 'Social', 'Pass']],
                  columns=['Hesaru', 'Subject', 'Grade'])
print(f'before changing column names : \n{df}')

df = df.rename(columns={'Hesaru': 'Name', 'Grade': 'Marks'})
print(f'after changing column names : \n{df}')
