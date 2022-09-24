# 완주하지 못한 선수

def solution(participant, completion): hash ={} for i in participant: if i in hash: hash[i] += 1 else: hash[i] = 1 for i in completion: if hash[i] == 1: del hash[i] else: hash[i] -= 1 answer = list(hash.keys())[0] return answer

# 전화번호 목록

def solution(phone_book): answer = True finish = False phone_book = sorted(phone_book, key=len) for i in range(0, len(phone_book)): if finish: break current = phone_book[i] for j in range(i+1, len(phone_book)): comp = phone_book[j] if len(current)<len(comp) and current == comp[0:len(current)]: answer = False finish = True break return answer #성공

# 위장

def solution(clothes): closet = dict() num_category = [] answer = 1 for name, category in clothes: if category in closet: closet[category].append(name) else: closet[category] = [name] for key in closet.keys(): num_category.append(len(closet[key])) for i in num_category: answer *= (i+1) answer -= 1 return answer #성공

# 베스트앨범

def solution(genres, plays): song = dict() sum_play = dict() n = len(genres) answer = [] for i in range(n): genre = genres[i] num_play = plays[i] if genre in song: song[genre].append([(-1)*num_play, i]) song[genre].sort() else: song[genre] = [[(-1)*num_play, i]] if genre in sum_play: sum_play[genre] += num_play else: sum_play[genre] = num_play sorted_list = [] for k in sum_play.keys(): sorted_list.append([sum_play[k], k]) sorted_list.sort(reverse=True) for _, g in sorted_list: for i in range(2): answer.append(song[g][i][1]) if len(song[g]) == 1: break return answer

