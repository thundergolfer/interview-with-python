# Find Anagrams In List

Given a **long** list of words, and a *target word*, find and return all words from the list that are an anagram of the target.

This function will be run many times so aim for a solution that is efficient when run over and over again on the same list.

#### Note: Technical Interview question at Zendesk (Undergraduate Internship)

```python
lst = ['dog','apple','odg','pen'] # list will be much longer
find_anagrams( 'god', lst )
> ['dog', 'odg']
find_anagrams( 'pelap', lst)
> ['apple']
# etc, etc 

```
