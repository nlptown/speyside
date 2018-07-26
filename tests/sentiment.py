import spacy
from tqdm import tqdm


def read_file(f):
    texts, labels = [], []
    with open(f) as i:
        for line in i:
            label = line[:10]
            text = line[10:].strip()
            label = {"positive": 1, "negative": 0} if label == "__label__2" else {"negative": 1, "positive": 0}
            texts.append(text)
            labels.append(label)
    return texts, labels


def evaluate(predicted_labels, gold_labels):
    tp = 1e-8  # True positives
    fp = 1e-8  # False positives
    fn = 1e-8  # False negatives
    tn = 1e-8  # True negatives
    for predicted, gold in zip(predicted_labels, gold_labels):
        for label, score in predicted.items():
            if score >= 0.5 and gold[label] >= 0.5:
                tp += 1.
            elif score >= 0.5 and gold[label] < 0.5:
                fp += 1.
            elif score < 0.5 and gold[label] < 0.5:
                tn += 1
            elif score < 0.5 and gold[label] >= 0.5:
                fn += 1

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f_score = 2 * (precision * recall) / (precision + recall)
    return {'textcat_p': precision, 'textcat_r': recall, 'textcat_f': f_score}


def test_sentiment():
    nlp = spacy.load("en_sentiment_reviews_sm")
    texts, gold_labels = read_file("tests/data/sentiment/test.txt")

    predicted_labels = []
    for text in tqdm(texts):
        doc = nlp(text)
        predicted_labels.append(doc.cats)

    scores = evaluate(predicted_labels, gold_labels)

    print(scores)

    assert scores["textcat_p"] >= 0.9439049999999556
    assert scores["textcat_r"] >= 0.9439049999999556
    assert scores["textcat_f"] >= 0.9439049999999556