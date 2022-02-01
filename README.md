# koyunkirpan
Source code for u/koyunkirpan

This repo is just a showcase for the source code and wasn't intented for providing a ready-to-use product for others. However, feel free to use, modify and share the code.

## Backstory
I was trying to make a small contest where I would create a bot account on reddit that comments on posts once in a while and then people would try to find this account by inspecting the subreddit activity. Back then, koyunkirpan was only able to make single comments on posts using their titles. Later on, people loved koyunkirpan because of its authenticity, simplicity and complex responses. Then I decided to keep koyunkirpan running. In less then six months, koyunkirpan reached 170k karma in his account, exceeding my own karma count, which makes me proud as hell. We also created a subreddit for koyunkirpan, where people share screenshots of funny conversations they've had with koyunkirpan.

You can check it here: [r/koyunkirpan](https://koyunkirpan.reddit.com) (for Turkish speakers)

## How does it work?
At the beginning, I've tried several things for koyunkirpan. But none of the solutions were good enough. They were inconsistent, silly and not suited to the subreddit's context. Then, while I was drinking a few beers, I came up with a stupid solution that just worked. I called it "the koyunkirpan algorithm". Yes, koyunkirpan does not have artifical intelligence, does not use machine learning models and isn't an oracle machine :)

Trying to analyze text context was amazingly hard because of the diversity of the Turkish language. But the semantic of the text was always related to its syntax! So, I wrote a simple algorithm that searched through reddit for keywords in the source text. Here I've used a special search combination for reddit where keywords in the source text were combined together in some kind of a disjunctive normal form (DNF). The highest results always include most of the keywords in some sense. After that, the algorithm collects comments similar to the source text and collects their replies. After ranking the results, it just picks a reply and return this as the response to the source text. Simple but highly suited for a community!

Here's an example of the idea. Imagine you're asking me a question and I don't know the answer but I'm trying to look like I know the answer. So, I go to a university and wander around searching for people that ask similar questions to my original question. I listen to professors' answers, collect them, and then decide on an answer by ranking them. After that I return and just give you the selected answer.

## Contribution
koyunkirpan is not a piece of software nor a product. It's a living piece of art that can be seen as the collective consciousness of users from r/KGBTR. Each day, koyunkirpan continues to amaze more people as he imitates comments made by real people. Therefore, I don't consider merging any pull requests.
