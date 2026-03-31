# 파일이름 : main.py
# 작 성 자 : 고준하

bucket_list = []
res1 = input(f"식당을 입력하세요: "); bucket_list.append(res1)
res2 = input(f"식당을 입력하세요: "); bucket_list.append(res2)
res3 = input(f"식당을 입력하세요: "); bucket_list.append(res3)
print(f"방문할 식당 목록: {bucket_list} \n")

res0 = input(f"1순위 식당을 입력하세요: "); bucket_list.insert(0, res0)
print(f"방문할 식당 목록: {bucket_list} \n")

res_today = input(f"오늘 방문한 식당을 입력하세요: "); bucket_list.remove(res_today)
print(f"방문할 식당 목록: {bucket_list}")