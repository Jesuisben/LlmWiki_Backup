import math

# 데이터
data = [
    ["A", 170, 3000],
    ["B", 180, 8000],
    ["C", 165, 2800],
    ["D", 175, 4500],
    ["E", 160, 2500],
    ["F", 185, 9000],
    ["G", 172, 3800],
    ["H", 178, 6500],
    ["I", 168, 3200],
    ["J", 182, 7500]
]

# ---------------------------
# 1. 원본 데이터 분리
# ---------------------------
heights = [row[1] for row in data]
salaries = [row[2] for row in data]

# ---------------------------
# 2. 정규화(Min-Max Scaling)
# ---------------------------
h_min = min(heights)
h_max = max(heights)

s_min = min(salaries)
s_max = max(salaries)

# ---------------------------
# 3. 표준화(Standardization)
# ---------------------------
h_mean = sum(heights) / len(heights)
s_mean = sum(salaries) / len(salaries)

# 모집단 표준편차
h_std = math.sqrt(
    sum((x - h_mean) ** 2 for x in heights) / len(heights)
)

s_std = math.sqrt(
    sum((x - s_mean) ** 2 for x in salaries) / len(salaries)
)

# ---------------------------
# 4. 결과 출력
# ---------------------------
print("=" * 100)
print(
    f"{'사람':<5}"
    f"{'키':>8}"
    f"{'연봉':>10}"
    f"{'정규화(키)':>15}"
    f"{'정규화(연봉)':>15}"
    f"{'표준화(키)':>15}"
    f"{'표준화(연봉)':>15}"
)
print("=" * 100)

for person, height, salary in data:

    # 정규화
    height_norm = (height - h_min) / (h_max - h_min)
    salary_norm = (salary - s_min) / (s_max - s_min)

    # 표준화
    height_std = (height - h_mean) / h_std
    salary_std = (salary - s_mean) / s_std

    print(
        f"{person:<5}"
        f"{height:>8}"
        f"{salary:>10}"
        f"{height_norm:>15.3f}"
        f"{salary_norm:>15.3f}"
        f"{height_std:>15.3f}"
        f"{salary_std:>15.3f}"
    )

max_height_person = max(data, key=lambda x: x[1])

print("\n[키가 가장 큰 사람]")
print(
    f"사람: {max_height_person[0]}, "
    f"키: {max_height_person[1]}cm, "
    f"연봉: {max_height_person[2]}만원"
)

# ---------------------------
# 6. 연봉 최대인 사람 찾기
# ---------------------------
max_salary_person = max(data, key=lambda x: x[2])

print("\n[연봉이 가장 높은 사람]")
print(
    f"사람: {max_salary_person[0]}, "
    f"키: {max_salary_person[1]}cm, "
    f"연봉: {max_salary_person[2]}만원"
)

# ---------------------------
# 7. 키 최소인 사람 찾기
# ---------------------------
min_height_person = min(data, key=lambda x: x[1])

print("\n[키가 가장 작은 사람]")
print(
    f"사람: {min_height_person[0]}, "
    f"키: {min_height_person[1]}cm, "
    f"연봉: {min_height_person[2]}만원"
)

# ---------------------------
# 8. 연봉 최소인 사람 찾기
# ---------------------------
min_salary_person = min(data, key=lambda x: x[2])

print("\n[연봉이 가장 낮은 사람]")
print(
    f"사람: {min_salary_person[0]}, "
    f"키: {min_salary_person[1]}cm, "
    f"연봉: {min_salary_person[2]}만원"
)