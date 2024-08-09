# ① 需求 2024/8/9日 针对df表中某列进行排序，倒叙或者是正序（实际场景:mysql存在重复接口，其中重复接口中存在接口名为空的信息，现在需要将其找出来）
import pandas


def pad_89():
    data89 = {"中文列": ['苹果', '香蕉', '苹果', '橙子', '香蕉', '葡萄'],
              "备注": ["", "gg", "aa", "cc", "", "pt"]}
    df89 = pandas.DataFrame(data89)
    # 针对中文列进行排序
    df89 = df89.sort_values(by="中文列", ascending=False)
    return df89
