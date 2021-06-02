# Section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본완성

"""
1. 단어 리스트 로드
2. 총 게임 시간 측정
3. 정답 개수 체크
"""

import random
import time

words = []                                   # 영어 단어 리스트 (1000개 로드)

n = 1                                        # 게임 시도 횟수
cor_cnt = 0                                  # 정답 개수

with open('./resource/word.txt', 'r') as f:  # 문제 txt 파일 로드
    for c in f:
        words.append(c.strip())              # 양 쪽 공백 제거

# print(words)                                 # 단어 리스트 확인

"""
['policy', 'number', 'such', 'please', 'available', 'copyright', 'support', 'message', 'after', 'best', 'software', 'then', 'jan', 'good', 'video', 'well', 'd', 'where', 'info', 'rights', 'public', 'books', 'high', 'school', 'through', 'm', 'each', 'links', 'she', 'review', 'years', 'order', 'very', 'privacy', 'book', 'items', 'company', 'r', 'read', 'group', 'sex', 'need', 'many', 'user', 'said', 'de', 'does', 'set', 'under', 'general', 'research', 'university', 'january', 'mail', 'full', 'map', 'reviews', 'program', 'life', 'know', 
'games', 'way', 'days', 'management', 'p', 'part', 'could', 'great', 'united', 'hotel', 'real', 'f', 'item', 'international', 'center', 'ebay', 'must', 'store', 'travel', 'comments', 'made', 'development', 'report', 'off', 'member', 'details', 'line', 'terms', 'before', 'hotels', 'did', 'send', 'right', 'type', 'because', 'local', 'those', 'using', 'results', 'office', 'education', 'national', 'car', 'design', 'take', 'posted', 'internet', 'address', 'community', 'within', 'states', 'area', 'want', 'phone', 'dvd', 'shipping', 'reserved', 'subject', 'between', 'forum', 'family', 'l', 'long', 'based', 'w', 'code', 'show', 'o', 'even', 'black', 'check', 'special', 'prices', 'website', 'index', 'being', 'women', 'much', 'sign', 'file', 'link', 'open', 'today', 'technology', 'south', 'case', 'project', 'same', 'pages', 'uk', 'version', 'section', 'own', 'found', 'sports', 'house', 'related', 'security', 'both', 'g', 'county', 'american', 'photo', 'game', 'members', 'power', 'while', 'care', 'network', 'down', 'computer', 'systems', 'three', 'total', 'place', 'end', 'following', 'download', 'h', 'him', 'without', 'per', 'access', 'think', 'north', 'resources', 'current', 'posts', 'big', 'media', 'law', 'control', 'water', 'history', 'pictures', 'size', 'art', 'personal', 'since', 'including', 'guide', 'shop', 'directory', 'board', 'location', 'change', 'white', 'text', 'small', 'rating', 'rate', 'government', 'children', 'during', 'usa', 'return', 'students', 'v', 'shopping', 'account', 'times', 'sites', 'level', 'digital', 'profile', 'previous', 'form', 'events', 'love', 'old', 'john', 'main', 'call', 'hours', 'image', 'department', 'title', 'description', 'non', 'k', 'y', 'insurance', 'another', 'why', 'shall', 'property', 'class', 'cd', 'still', 'money', 'quality', 'every', 'listing', 'content', 'country', 'private', 'little', 'visit', 'save', 'tools', 'low', 'reply', 'customer', 'december', 'compare', 'movies', 'include', 'college', 'value', 'article', 'york', 'man', 'card', 'jobs', 'provide', 'j', 'food', 'source', 'author', 'different', 'press', 'u', 'learn', 'sale', 'around', 'print', 'course', 'job', 'canada', 'process', 'teen', 'room', 'stock', 'training', 'too', 'credit', 'point', 'join', 'science', 'men', 'categories', 'advanced', 'west', 'sales', 'look', 'english', 'left', 'team', 'estate', 'box', 'conditions', 'select', 'windows', 'photos', 'gay', 'thread', 'week', 'category', 'note', 'live', 'large', 'gallery', 'table', 'register', 'however', 'june', 'october', 'november', 'market', 'library', 'really', 'action', 'start', 'series', 'model', 'features', 'air', 'industry', 'plan', 'human', 'provided', 'tv', 'yes', 'required', 'second', 'hot', 'accessories', 'cost', 'movie', 'forums', 'march', 'la', 'september', 'better', 'say', 'questions', 'july', 'yahoo', 'going', 'medical', 'test', 'friend', 'come', 'dec', 'server', 'pc', 'study', 'application', 'cart', 'staff', 'articles', 'san', 'feedback', 'again', 'play', 'looking', 'issues', 'april', 'never', 'users', 'complete', 'street', 'topic', 'comment', 'financial', 'things', 'working', 'against', 'standard', 'tax', 'person', 'below', 'mobile', 'less', 'got', 'blog', 'party', 'payment', 'equipment', 'login', 'student', 'let', 'programs', 'offers', 'legal', 'above', 'recent', 'park', 'stores', 'side', 'act', 'problem', 'red', 'give', 'memory', 'performance', 'social', 'q', 'august', 'quote', 'language', 'story', 'sell', 'options', 'experience', 'rates', 'create', 'key', 'body', 'young', 'america', 'important', 'field', 'few', 'east', 'paper', 'single', 'ii', 'age', 'activities', 'club', 'example', 'girls', 'additional', 'password', 'z', 'latest', 'something', 'road', 'gift', 'question', 'changes', 'night', 'ca', 'hard', 'texas', 'oct', 'pay', 'four', 'poker', 'status', 'browse', 'issue', 'range', 'building', 'seller', 'court', 'february', 'always', 'result', 'audio', 'light', 'write', 'war', 'nov', 'offer', 'blue', 'groups', 'al', 'easy', 'given', 'files', 'event', 'release', 'analysis', 'request', 'fax', 'china', 'making', 'picture', 'needs', 'possible', 'might', 'professional', 'yet', 'month', 'major', 'star', 'areas', 'future', 'space', 'committee', 'hand', 'sun', 'cards', 'problems', 'london', 'washington', 'meeting', 'rss', 'become', 'interest', 'id', 'child', 'keep', 'enter', 'california', 'porn', 'share', 'similar', 'garden', 'schools', 'million', 'added', 'reference', 'companies', 'listed', 'baby', 'learning', 'energy', 'run', 'delivery', 'net', 'popular', 'term', 'film', 'stories', 'put', 'computers', 'journal', 'reports', 'co', 'try', 'welcome', 'central', 'images', 'president', 'notice', 'god', 'original', 'head', 'radio', 'until', 'cell', 'color', 'self', 'council', 'away', 'includes', 'track', 'australia', 'discussion', 'archive', 'once', 'others', 'entertainment', 'agreement', 'format', 'least', 'society', 'months', 'log', 'safety', 'friends', 'sure', 'faq', 'trade', 'edition', 'cars', 'messages', 'marketing', 'tell', 'further', 'updated', 'association', 'able', 'having', 'provides', 'david', 'fun', 'already', 'green', 'studies', 'close', 'common', 'drive', 'specific', 'several', 'gold', 'feb', 'living', 'sep', 'collection', 'called', 'short', 'arts', 'lot', 'ask', 'display', 'limited', 'powered', 'solutions', 'means', 'director', 'daily', 'beach', 'past', 'natural', 'whether', 'due', 'et', 'electronics', 'five', 'upon', 'period', 'planning', 'database', 'says', 'official', 'weather', 'mar', 'land', 'average', 'done', 'technical', 'window', 'france', 'pro', 'region', 'island', 'record', 'direct', 'microsoft', 'conference', 'environment', 'records', 'st', 'district', 'calendar', 'costs', 'style', 'url', 'front', 'statement', 'update', 'parts', 'aug', 'ever', 'downloads', 'early', 'miles', 'sound', 'resource', 'present', 'applications', 'either', 'ago', 'document', 'word', 'works', 'material', 'bill', 'apr', 'written', 'talk', 'federal', 'hosting', 'rules', 'final', 'adult', 'tickets', 'thing', 'centre', 'requirements', 'via', 'cheap', 'nude', 'kids', 'finance', 'true', 'minutes', 'else', 'mark', 
'third', 'rock', 'gifts', 'europe', 'reading', 'topics', 'bad', 'individual', 'tips', 'plus', 'auto', 'cover', 'usually', 'edit', 'together', 'videos', 'percent', 'fast', 'function', 'fact', 'unit', 'getting', 'global', 'tech', 'meet', 'far', 'economic', 'en', 'player', 'projects', 'lyrics', 'often', 'subscribe', 'submit', 'germany', 'amount', 'watch', 'included', 'feel', 'though', 'bank', 'risk', 'thanks', 'everything', 'deals', 'various', 'words', 'linux', 'jul', 'production', 'commercial', 'james', 'weight', 'town', 'heart', 'advertising', 'received', 'choose', 'treatment', 'newsletter', 'archives', 'points', 'knowledge', 'magazine', 'error', 'camera', 'jun', 'girl', 'currently', 'construction', 'toys', 'registered', 'clear', 'golf', 'receive', 'domain', 'methods', 'chapter', 'makes', 'protection', 'policies', 'loan', 'wide', 'beauty', 'manager', 'india', 'position', 'taken', 'sort', 'listings', 'models', 'michael', 'known', 'half', 'cases', 'step', 'engineering', 'florida', 'simple', 'quick', 'none', 'wireless', 'license', 'paul', 'friday', 'lake', 'whole', 'annual', 'published', 'later', 'basic', 'sony', 'shows', 'corporate', 'google', 'church', 'method', 'purchase', 'customers', 'active', 'response', 'practice', 'hardware', 'figure', 'materials', 'fire', 'holiday', 'chat', 'enough', 'designed', 'along', 'among', 'death', 'writing', 'speed', 'html', 'countries', 'loss', 'face', 'brand', 'discount', 'higher', 'effects', 'created', 'remember', 'standards', 'oil', 'bit', 'yellow', 'political', 'increase', 'advertise', 'kingdom', 'base', 'near', 'environmental', 'thought', 'stuff', 'french', 
'storage', 'oh', 'japan', 'doing', 'loans', 'shoes', 'entry', 'stay', 'nature', 'orders', 'availability', 'africa', 'summary', 'turn', 
'mean', 'growth', 'notes', 'agency', 'king', 'monday', 'european', 'activity', 'copy', 'although', 'drug', 'pics', 'western', 'income', 'force', 'cash', 'employment', 'overall', 'bay', 'river', 'commission', 'ad', 'package', 'contents', 'seen', 'players', 'engine', 'port', 'album', 'regional', 'stop', 'supplies', 'started', 'administration', 'bar', 'institute', 'views', 'plans', 'double', 'dog', 'build', 'screen', 'exchange', 'types', 'soon', 'sponsored', 'lines', 'electronic', 'continue', 'across', 'benefits', 'needed', 'season', 'apply', 'someone', 'held', 'ny', 'anything', 'printer', 'condition', 'effective', 'believe', 'organization', 'effect', 'asked', 'eur', 'mind', 'sunday', 'selection', 'casino', 'pdf', 'lost', 'tour', 'menu', 'volume', 'cross', 'anyone', 'mortgage', 'hope', 'silver', 'corporation', 'wish', 'inside', 'solution', 'mature', 'role', 'rather', 'weeks', 'addition', 'came', 'supply', 'nothing', 'certain', 'usr', 
'executive', 'running', 'lower', 'necessary', 'union', 'jewelry', 'according', 'dc', 'clothing', 'mon', 'com', 'particular', 'fine', 'names', 'robert', 'homepage', 'hour', 'gas', 'skills', 'six', 'bush', 'islands', 'advice', 'career', 'military', 'rental', 'decision', 'leave', 'british', 'teens', 'pre', 'huge', 'sat', 'woman', 'facilities', 'zip', 'bid', 'kind', 'sellers', 'middle', 'move', 'cable', 'opportunities', 'taking', 'values', 'division', 'coming', 'tuesday', 'object', 'lesbian', 'appropriate', 'machine', 'logo', 'length', 'actually', 'nice', 'score', 'statistics', 'client', 'ok', 'returns', 'capital', 'follow', 'sample', 'investment', 'sent', 'shown', 'saturday', 'christmas', 'england', 'culture', 'band', 'flash', 'ms', 'lead', 'george', 'choice', 'went', 'starting', 'registration', 'fri', 'thursday', 'courses', 'consumer', 'hi', 'airport', 'foreign', 'artist', 'outside', 'furniture', 'levels', 'channel', 'letter', 'mode', 'phones', 'ideas', 'wednesday', 'structure', 'fund', 'summer', 'allow', 'degree', 'contract', 'button', 'releases', 'wed', 'homes', 'super', 'male', 'matter', 'custom', 'virginia', 'almost', 'took', 'located', 'multiple', 'asian', 'distribution', 'editor', 'inn', 'industrial', 'cause', 'potential', 'song', 'cnet', 'ltd', 'los', 'hp', 'focus', 'late', 'fall', 'featured', 'idea', 'rooms', 'female', 'responsible', 'inc', 'communications', 'win', 'associated', 'thomas', 'primary', 'cancer', 'numbers', 'reason', 'tool', 'browser', 'spring', 'foundation', 'answer', 'voice', 'eg', 'friendly', 'schedule', 'documents', 'communication', 'purpose', 'feature', 'bed', 'comes', 
'police', 'everyone', 'independent', 'ip', 'approach', 'cameras', 'brown', 'physical', 'operating', 'hill', 'maps', 'medicine', 'deal', 'hold', 'ratings', 'chicago', 'forms', 'glass', 'happy', 'tue', 'smith', 'wanted', 'developed', 'thank', 'safe', 'unique', 'survey', 'prior', 'telephone', 'sport', 'ready', 'feed', 'animal', 'sources', 'mexico', 'population', 'pa', 'regular', 'secure', 'navigation', 'operations', 'therefore', 'ass', 'simply', 'evidence', 'station', 'christian', 'round', 'paypal', 'favorite', 'understand', 'option', 'master', 'valley', 'recently', 'probably', 'thu', 'rentals', 'sea', 'built', 'publications', 'blood', 'cut', 'worldwide', 'improve', 'connection', 'publisher', 'hall', 'larger', 'anti', 'networks', 'earth', 'parents', 'nokia', 'impact', 'transfer', 'introduction', 'kitchen', 'strong', 'tel', 'carolina', 'wedding', 'properties', 'hospital', 'ground', 'overview', 'ship', 'accommodation', 'owners', 'disease', 'tx', 'excellent', 'paid', 'italy', 'perfect', 'hair', 'opportunity', 'kit', 'classic', 'basis', 'command', 'cities', 'william', 'express', 'anal', 'award', 'distance', 'tree', 'peter', 'assessment', 'ensure', 'thus', 'wall', 'ie', 'involved', 'el', 'extra', 'especially', 'interface', 'pussy', 'partners', 'budget', 'rated', 'guides', 'success', 'maximum', 'ma', 'operation', 'existing', 'quite', 'selected', 'boy', 'amazon', 'patients', 'restaurants', 'beautiful', 'warning', 'wine', 'locations', 'horse', 'vote', 'forward', 'flowers', 'stars', 'significant', 'lists', 'technologies', 'owner', 'retail', 'animals', 'useful', 'directly', 'manufacturer', 'ways', 'est', 'son', 'providing', 'rule', 'mac', 'housing', 'takes', 'iii', 'gmt', 'bring', 'catalog', 'searches', 'max', 'trying', 'mother', 'authority', 'considered', 'told', 'xml', 'traffic', 'programme', 'joined', 'input', 'strategy', 'feet', 'agent', 'valid', 'bin', 'modern', 'senior', 'ireland', 'sexy', 'teaching', 'door', 'grand', 'testing', 'trial', 'charge', 'units', 'instead', 'canadian', 'cool', 'normal', 
'wrote', 'enterprise', 'ships', 'entire', 'educational', 'md', 'leading', 'metal', 'positive', 'fl', 'fitness', 'chinese', 'opinion', 'mb', 'a
"""

input("Ready? Press Enter Key!")             # Enter Game Start!

start = time.time()                          # Start Time

while n <= 5:                                # 5회 반복
    random.shuffle(words)                    # List shuffle!
    q = random.choice(words)                 # List -> words random extract!

    print()

    print("*Question # {}".format(n))
    print(q)                                 # 문제 출력

    x = input()                              # 타이핑 입력
    
    print()
    
    if str(q).strip() == str(x).strip():     # 입력 확인 (공백제거)
        print("Pass!")
        cor_cnt += 1                         # 정답 개수 카운트
    else:
        print("Wrong!")

    n += 1                                   # 다음 문제 전환

end = time.time()                            # End Time
et = end - start                             # 총 게임 시간
et = format(et, ".3f")                       # 소수 셋째 자리 출력 (시간)

if cor_cnt >= 3:                             # 3개 이상 합격
    print("합격")
else:
    print("불합격")
    
# 수행 시간 출력
print("게임 시간 :", et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작지점
if __name__ == '__main__':
    pass

"""
Ready? Press Enter Key!

*Question # 1
downloaded
downloaded

Pass!

*Question # 2
continued
contined

Wrong!

*Question # 3
chemistry
chemistry

Pass!

*Question # 4
footage
footage

Pass!

*Question # 5
irc
irc

Pass!
합격
게임 시간 : 13.396 초 정답 개수 : 4
"""