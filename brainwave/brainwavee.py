import re

def blogwave(text):
    pattern = r"এটি|ইহা"
    rp = "এটা"
    string = text
    ans = re.sub(pattern, rp, string)

    pattern = r"দেখুন না|তাকান না|তাকাবেন না"
    rp = "বিকল্প নেই"
    string = text
    ans1 = re.sub(pattern, rp, ans)
    
    pattern = r"কুড়ি"
    rp = "টেস্ট"

    ans2 = re.sub(pattern, rp, ans1)
    pattern = r"নিখুঁত পছন্দ"
    rp = "বেস্ট অপশন"

    ans3 = re.sub(pattern, rp, ans2)
    pattern = r"অনুবাদিত"
    rp = "{{name}}"

    ans4 = re.sub(pattern, rp, ans3)
    pattern = r"নিখুঁত|উপযুক্ত"
    rp = "পারফেক্ট"

    ans5 = re.sub(pattern, rp, ans4)
    pattern = r" উন্মুখ|উপলব্ধ"
    rp = "Ready"

    ans6 = re.sub(pattern, rp, ans5)

    ans7 = re.sub(pattern, rp, ans6)
    pattern = r"শ্রবণ "
    rp = "শোনা"

    ans6 = re.sub(pattern, rp, ans5)
    return ans7


    return ans

def adify(text):
    pattern = r"দেখুন না|তাকান না|তাকাবেন না"
    rp = "বিকল্প নেই"
    string = text
    ans1 = re.sub(pattern, rp, string)
    
    pattern = r"কুড়ি"
    rp = "টেস্ট"

    ans2 = re.sub(pattern, rp, ans1)
    pattern = r"নিখুঁত পছন্দ"
    rp = "বেস্ট অপশন"

    ans3 = re.sub(pattern, rp, ans2)
    pattern = r"অনুবাদিত"
    rp = "{{name}}"

    ans4 = re.sub(pattern, rp, ans3)
    pattern = r"নিখুঁত|উপযুক্ত"
    rp = "পারফেক্ট"

    ans5 = re.sub(pattern, rp, ans4)
    pattern = r" উন্মুখ|উপলব্ধ"
    rp = "Ready"

    ans6 = re.sub(pattern, rp, ans5)

    ans7 = re.sub(pattern, rp, ans6)
    pattern = r"শ্রবণ "
    rp = "শোনা"

    ans6 = re.sub(pattern, rp, ans5)
    return ans7

