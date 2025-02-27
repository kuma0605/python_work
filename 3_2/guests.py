guests = ["小美","小帅","大美","大帅"]
# 小帅无法参加，需邀请另外一位嘉宾
print("小帅")
guests.pop(1)
guests.insert(1,"小帅帅")
print(guests)
# 找到一个更大的餐桌，可以邀请更多的嘉宾
print("找到一个更大的餐桌")
guests.insert(0,"小美美")
guests.insert(2,"小帅帅")
guests.append("大帅帅")
print(guests)
# 由于新餐桌无法及时送达，只能邀请两位嘉宾
print(f"嘉宾列表长度为：{len(guests)}")
print("由于新餐桌无法及时送达，只能邀请两位嘉宾")
print(f"很抱歉，{guests.pop()}，无法邀请你来共进晚餐")
print(f"很抱歉，{guests.pop()}，无法邀请你来共进晚餐")
print(f"很抱歉，{guests.pop()}，无法邀请你来共进晚餐")
