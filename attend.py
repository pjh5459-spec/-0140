"""
스터디 출석부 프로그램 (attend.py)
- 외부 라이브러리 없이 표준 라이브러리만 사용
- 데이터는 attendance.csv 파일에 저장
"""

import csv
import os
from datetime import datetime

# ── 설정 ──────────────────────────────────────────
DATA_FILE = "attendance.csv"   # 출석 데이터 저장 파일
HEADER    = ["날짜", "이름"]   # CSV 헤더


# ── 파일 초기화 ───────────────────────────────────
def init_file():
    """데이터 파일이 없으면 헤더를 포함해 새로 만든다."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="", encoding="utf-8-sig") as f:
            csv.writer(f).writerow(HEADER)


# ── 출석 추가 ─────────────────────────────────────
def add_attendance(date: str, name: str):
    """날짜·이름을 받아 CSV에 한 줄 추가한다."""
    # 날짜 형식 검증 (YYYY-MM-DD)
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("  ⚠  날짜 형식이 올바르지 않습니다. 예) 2025-06-10")
        return

    name = name.strip()
    if not name:
        print("  ⚠  이름을 입력해 주세요.")
        return

    # 중복 체크
    records = load_records()
    if any(r["날짜"] == date and r["이름"] == name for r in records):
        print(f"  ⚠  [{date}] {name} 님은 이미 출석 처리되어 있습니다.")
        return

    with open(DATA_FILE, "a", newline="", encoding="utf-8-sig") as f:
        csv.writer(f).writerow([date, name])
    print(f"  ✔  [{date}] {name} 님 출석 완료!")


# ── 전체 기록 불러오기 ────────────────────────────
def load_records() -> list[dict]:
    """CSV 파일을 읽어 딕셔너리 리스트로 반환한다."""
    with open(DATA_FILE, "r", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


# ── 출석 목록 출력 ────────────────────────────────
def show_all():
    """전체 출석 기록을 날짜 → 이름 순으로 정렬해 출력한다."""
    records = load_records()
    if not records:
        print("  (출석 기록이 없습니다.)")
        return

    records.sort(key=lambda r: (r["날짜"], r["이름"]))

    print()
    print(f"  {'날짜':<14} {'이름'}")
    print("  " + "-" * 28)
    for r in records:
        print(f"  {r['날짜']:<14} {r['이름']}")
    print(f"\n  총 {len(records)}건")


# ── 날짜별 출석 조회 ──────────────────────────────
def show_by_date(date: str):
    """특정 날짜의 출석자 목록을 출력한다."""
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("  ⚠  날짜 형식이 올바르지 않습니다. 예) 2025-06-10")
        return

    records = [r for r in load_records() if r["날짜"] == date]
    if not records:
        print(f"  [{date}] 출석 기록이 없습니다.")
        return

    records.sort(key=lambda r: r["이름"])
    print(f"\n  [{date}] 출석자 목록")
    print("  " + "-" * 20)
    for i, r in enumerate(records, 1):
        print(f"  {i:>2}. {r['이름']}")
    print(f"\n  총 {len(records)}명")


# ── 이름별 출석 조회 ──────────────────────────────
def show_by_name(name: str):
    """특정 이름의 출석 날짜 목록을 출력한다."""
    name = name.strip()
    records = [r for r in load_records() if r["이름"] == name]
    if not records:
        print(f"  [{name}] 출석 기록이 없습니다.")
        return

    records.sort(key=lambda r: r["날짜"])
    print(f"\n  [{name}] 출석 날짜 목록")
    print("  " + "-" * 20)
    for i, r in enumerate(records, 1):
        print(f"  {i:>2}. {r['날짜']}")
    print(f"\n  총 {len(records)}회")


# ── 출석 삭제 ─────────────────────────────────────
def delete_attendance(date: str, name: str):
    """날짜·이름이 일치하는 출석 기록 한 건을 삭제한다."""
    name = name.strip()
    records = load_records()
    new_records = [r for r in records
                   if not (r["날짜"] == date and r["이름"] == name)]

    if len(new_records) == len(records):
        print(f"  ⚠  [{date}] {name} 님의 출석 기록을 찾을 수 없습니다.")
        return

    with open(DATA_FILE, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(new_records)
    print(f"  🗑  [{date}] {name} 님의 출석 기록을 삭제했습니다.")


# ── 메뉴 출력 ─────────────────────────────────────
def print_menu():
    print()
    print("=" * 36)
    print("       📋  스터디 출석부")
    print("=" * 36)
    print("  1. 출석 추가")
    print("  2. 전체 목록 보기")
    print("  3. 날짜별 조회")
    print("  4. 이름별 조회")
    print("  5. 출석 삭제")
    print("  0. 종료")
    print("=" * 36)


# ── 메인 루프 ─────────────────────────────────────
def main():
    init_file()

    while True:
        print_menu()
        choice = input("  메뉴 선택 → ").strip()

        if choice == "1":
            print()
            date = input("  날짜 입력 (예: 2025-06-10) → ").strip()
            name = input("  이름 입력 → ").strip()
            add_attendance(date, name)

        elif choice == "2":
            show_all()

        elif choice == "3":
            print()
            date = input("  조회할 날짜 (예: 2025-06-10) → ").strip()
            show_by_date(date)

        elif choice == "4":
            print()
            name = input("  조회할 이름 → ").strip()
            show_by_name(name)

        elif choice == "5":
            print()
            date = input("  삭제할 날짜 (예: 2025-06-10) → ").strip()
            name = input("  삭제할 이름 → ").strip()
            delete_attendance(date, name)

        elif choice == "0":
            print("\n  프로그램을 종료합니다. 👋\n")
            break

        else:
            print("  ⚠  0~5 중에서 선택해 주세요.")

        input("\n  [Enter] 키를 누르면 메뉴로 돌아갑니다...")


if __name__ == "__main__":
    main()
