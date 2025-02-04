# pyinstaller
def calculate_bb100(bb, hands_played, winnings):

    if hands_played == 0:
        return 0
    return (winnings / (bb/100)) / (hands_played/100) 

if __name__ == "__main__":
    while(1):
        bb = float(input("NL幾(1BB的金額*100): "))
        hands_played = int(input("\n手數: "))
        winnings_yellow = float(input("\n黃線: "))
        winnings_green = float(input("\n綠線: "))

        bb100_yellow = calculate_bb100(bb, hands_played, winnings_yellow)
        bb100_green = calculate_bb100(bb, hands_played, winnings_green)
        print(f"\n你的 黃線BB/100 是: {bb100_yellow:.2f}")
        print(f"\n你的 綠線BB/100 是: {bb100_green:.2f}")
        
