# Custom faithfulness score
def calculate_faithfulness(answer, source_documents):
    source_sentences = [sent.strip() for doc in source_documents for sent in doc.split('.')]
    answer_sentences = answer.split('.')

    faithful_score = sum(any(ans_sent in src_sent for src_sent in source_sentences)
                         for ans_sent in answer_sentences) / len(answer_sentences)

    return faithful_score


# Using similarity - did not work because the transformer model wasn't loading properly

# from transformers import AutoModelForSequenceClassification, AutoTokenizer
# import torch
#
# # Load a pre-trained model and tokenizer for semantic similarity
# model_name = "sentence-transformers/all-MiniLM-L6-v2"
# model = AutoModelForSequenceClassification.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)
#
#
# def calculate_faithfulness(answer, source_documents):
#     source_text = ' '.join(source_documents)
#     inputs = tokenizer(answer, source_text, return_tensors="pt", padding=True, truncation=True)
#     with torch.no_grad():
#         outputs = model(**inputs)
#         similarity = torch.sigmoid(outputs.logits).item()
#
#     return similarity
