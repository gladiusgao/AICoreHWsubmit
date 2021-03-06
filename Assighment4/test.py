# -*- coding: UTF-8 -*
# 测试
import tensorflow.contrib.keras as kr
import torch
from torch import nn
from cnews_loader import read_category, read_vocab
from model import TextRNN
import numpy as np
 
vocab_file = 'cnews.vocab.txt'
 
class RnnModel:
    def __init__(self):
        self.categories, self.cat_to_id = read_category()
        self.words, self.word_to_id = read_vocab(vocab_file)
        self.model = TextRNN()
        self.model.load_state_dict(torch.load('model_params.pkl'))
 
    def predict(self, message):
        content = message
        data = [self.word_to_id[x] for x in content if x in self.word_to_id]
        data = kr.preprocessing.sequence.pad_sequences([data], 600)
        data = torch.LongTensor(data)
        y_pred_cls = self.model(data)
        class_index = torch.argmax(y_pred_cls[0]).item()
        return self.categories[class_index]
 
 
if __name__ == '__main__':
    model = RnnModel()
    test_demo = ['天才中锋崇拜王治郅 周琦：球员最终是靠实力说话2月14日从土耳其男篮邀请赛回到北京之后，周琦马上转机返回辽宁，由于之前比赛打得很辛苦，再加之时差的问题，第二天他一觉睡到了中午。接下来的两天里，周琦感觉比在赛场还要辛苦，因为既要继续坚持训练，还要应付多家媒体的采访邀请，这可是小周琦以前从未遇到过的事情，太多的短信和电话让他的手机一度“瘫痪”。“其实我真不愿意说，我现在还没什么成绩呢。”只有15岁就要应付如此大的荣誉和压力，周琦能否坚持住？“还好，我把他们都看成是督促我前进的动力就好了。”话题重新回到土耳其，周琦依然处在兴奋之中。说到刚刚过去的比赛，周琦说，虽然知道这只是一个邀请赛，而美国、西班牙等强国也没有参加，但是自己还是把它完全当成国际级的正式比赛来对待，“实战的机会毕竟很珍贵嘛。”周琦说。但是一到了赛场，周琦发现很多对手还是很有实力的，让他记忆最深刻的一场比赛不是决赛中险胜东道主土耳其，而是半决赛中与德国拼满3个加时，“那场真是打得很艰难，德国队员的顽强是世界闻名的，不过我们的作风也不输给他们，最后赢球了很高兴。”聪明的周琦不光记住了赢球，还在比赛中注意观察场上的对手，比如德国的一位中锋身体很强硬，而土耳其的中锋技术很扎实，比赛之后，周琦会将对手的表现熟记于心，然后吸取他们身上的长处，充实到自己的训练当中。尽管在接受采访时，周琦表示自己既不做第二个姚明，也不想做第二个王治郅，只想走自己的路，但是周琦的确将王治郅视为自己的偶像，训练或是比赛中的某些动作会不经意地模仿偶像。“我会给自己树立一个标杆，向着那样的方向去努力。无论外界对我有什么样的评价，我一直相信，球员最终是要靠实力说话的。']
                 
    for i in test_demo:
        print(i,":",model.predict(i))