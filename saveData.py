import procesos_info

def save_data(name1,name2):
	df_new=procesos_info.InfoProcess(name1,name2)
	df_new_copy=df_new
	file_name = 'test_process.xlsx'
	df_new_copy.to_excel(file_name,index=False) 
	print('DataFrame is written to Excel File successfully.')
