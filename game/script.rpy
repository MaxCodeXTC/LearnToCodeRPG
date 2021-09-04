﻿label start:
    # initialize variables
    python:
        player_name = renpy.input("What's your name? (Type something and hit Enter)")
        player_name = player_name.strip()
        if not player_name:
            player_name = "Lydia"
        persistent.player_name = player_name

        # stats system
        player_stats = {
        'Sanity': 100,
        'CS Knowledge': None,
        'Interview Skills': None,
        'Dev Skills': None,
        }
        # to loop over the dictionary deterministically
        player_stats_names = list(player_stats.keys())

    screen player_stats():
        ## Ensure this appears on top of other screens.
        zorder 100
        frame:
            # top left of screen
            xalign 0
            yalign 1
            xpadding 30
            ypadding 30

            hbox:
                spacing 40
                # left column
                vbox:
                    spacing 10
                    for stats_name in player_stats_names:
                        # if None, not yet initialized/unlocked
                        if player_stats[stats_name] is not None:
                            text stats_name color gui.accent_color
                # right column
                vbox:
                    spacing 10
                    for stats_name in player_stats_names:
                        # if None, not yet initialized/unlocked
                        if player_stats[stats_name] is not None:
                            text str(player_stats[stats_name])

label stage1_intro:
    show screen player_stats
    # Stage 2. player's decision to learn to code
    scene bg kid_home with dissolve
    mc "Okay, so that's it for today's session. I'll see you next week."
    kid "Oh sorry, can we do the week after next? I just heard about a new class that teaches you how to code and build robots and I need to check that out next week."
    mc "Sure, no problem. See you then."

    scene bg bedroom night with dissolve
    mc "It's crazy how everyone these days is learning to code. High school students even."
    mc "Six months then a six-figure job? That's even crazier."
    mc "Hmm, but I can see the appeal in that."
    mc "Maybe I can learn to code as well."
    mc "These bootcamp programs are expensive. Maybe I can go with free online resources first."
    mc "Let's see, what should we learn first? Python? JavaScript? Web Dev?"
    mc "Oh here's a video about the top 10 tech skills worth learning in 2021. Let's check that out!"

    $ player_stats['CS Knowledge'] = 0
    mc "So Java and JavaScript are different things? Wait, which one is for web dev again?"
    $ player_stats['CS Knowledge'] += 1
    mc "And there are print statements and print() functions. Which is for Python 2 and which is for Python 3? I remember one video saying that Python 2 is outdated but does that mean that I don't have to learn it?"
    $ player_stats['CS Knowledge'] += 1
    mc "Maybe I shouldn't bother with learning Python 3 even. Someone may just decide that Python 3 is too old-fashioned before I even get a chance to learn it."
    $ player_stats['CS Knowledge'] += 1
    mc "Java doesn't sound like a good idea either. People are so hyped about Kotlin."
    $ player_stats['CS Knowledge'] += 1
    mc "JavaScript? TypeScript?"
    $ player_stats['CS Knowledge'] += 1
    mc "Maybe I can find a job posting I like and start learning their required skills."
    mc "But what is front-end, back-end, or full-stack? What are the differences?"
    mc "DevOps?"
    mc "Why is this company using their pet coding language that nobody else uses?"
    mc "Ugh. This is so frustrating."
    mc "Learn to code? Haha. I know it can't be that easy."
    mc "There might be people who are cut out to do this, but definitely not me."

    # hard-reset player's CS knowledge :)
    $ player_stats['CS Knowledge'] = 0
    mc "The kid I'm tutoring is cutting down our sessions for his coding classes. Ugh. I still need to pay the bills. Let's see if the coffee shop next door is hiring."

label stage3_annika:
    # Stage 3. Annika

    # scene gray90 with Pause(1)
    # show text "{size=48}{color=#fff}{i}Annika{i}{/color}{/size}" with dissolve
    # with Pause(2)
    # scene gray90 with dissolve
    # with Pause(1)
    
    scene bg bedroom day with dissolve
    mc "My phone is beeping."
    mc "Who's calling me at this hour?"

    show annika

    annika "[persistent.player_name]! How have you been?"
    mc "Good. Just new grad blues. You?"

    show annika happy
    annika "Great! Well, I'm really excited. I just got a job!"
    annika "And, like, it's not just any job! It's a web development job!"
    annika "I get paid for building cool websites for others. Doesn't that sound great?"
    mc "Yeah. Wow. Congrats!"
    annika "Thanks!"
    mc "How hard was it for you? I also tried to learn to code for some time but it got too hard and I quit."

    show annika confused
    annika "I'm sorry to hear that but you should give coding another try!"
    annika "Hey, hear me out."
    annika "It wasn't like easy peasy for me either. Like neither of us majored in CS. The CS kids have a way easier time getting a tech job."
    mc "You did take some CS electives in school, no?"
    annika "Yeah but they are pretty rusty. And honestly, what you learn in school is so much different from real-world software engineering."

    show annika neutral
    annika "I mean, in school you learn about theories and stuff. Like I did take a Web Dev 101 back in school but we never built an entire website from scratch."
    annika "I never gave web design a second thought after the final exam."
    annika "I've been self-studying all these months with the help of some awesome free resources. I even built a pet adoption website for a side project and that's when I applied everything I learned about user experience, data models, and so on."
    annika "And there was this bug that I had no idea how to fix until..."
    annika "Oh sorry I've been talking all the time. I must have bored you with this tech talk stuff."
    mc "No worries. It does look like you are doing something you enjoy!"
    mc "That must be really cool. I wish I could be like you."
    annika "You totally can! Did I give you the link to the awesome resource that I've been using?"
    annika "It's called freeCodeCamp. Check that out!"
    mc "Thanks. I will."
    mc "Hey Annika. So I've been checking out freeCodeCamp as you suggested."
    mc "I think its curriculum looks solid."
    mc "It's honest hard work, though. And I'm not sure if I can make it through on my own... What if I run into something that I can't understand? What if there is an issue I can't solve? What if it gets too hard again and I lose my motivation?"
    annika "That's totally okay! In fact, what I love about freeCodeCamp is that they have an entire community that can help you out and cheer you on."
    annika "And I can be your go-to accountability buddy as well! Ping me anytime if anything comes up."
    mc "Thanks Annika. I know I can count on you."
    mc "Best of luck with your new job by the way! Let me know how it goes."

label stage7_ryan:
    # Stage 7. Ryan
    scene bg desk with dissolve
    show ryan

    ryan "Hi [persistent.player_name]. I'm Ryan. I'm a senior engineer at Colordeck."
    mc "Hi Ryan. Nice to meet you! I'm [persistent.player_name], a recent grad and developer wannabe."
    ryan "That sounds good."
    ryan "Why don't I start by telling you a bit about myself? Then ask whatever you want to know about me, my job, or tech in general."
    mc "Sounds good."
    ryan "It's a long story and a bumpy ride. So buckle up."
    ryan "I graduated from college some ten years ago. I majored in music and design so I worked as a freelance designer straight out of college."
    ryan "Freelancing gives me some freedom and flexibility at first, but I soon discovered that my skills weren't honed enough to attract large, established clients. And working with small, less established clients doesn't pay well and puts a lot of stress on a newbie freelancer."
    ryan "So I decided to upgrade my skills and try something new."
    ryan "I learned to design websites and got a job designing websites at a small local company."
    ryan "You know, at small companies, everyone does a little bit of everything."
    ryan "I was hired for my web design skills, but occasionally I would be asked to write some HTML, CSS, JavaScript to showcase the design I have in mind in action, not just on paper."
    ryan "I picked up a little HTML, CSS, JavaScript in those years and found them to be quite interesting."
    ryan "I then found out that there is a term for these skills, front-end development."
    ryan "I thought, cool, I've done some front-end development, maybe I can become a full-time front-end developer?"
    ryan "I started researching and teaching myself front-end dev. The Internet in my days didn't have nearly as many resources as nowadays. So I had to be extremely resourceful and develop my own learning path."
    ryan "It all paid off when I got my front-end development job at my current company. I've been with the company since. Nice culture, smart people, interesting work."
    mc "Wow."
    ryan "Yeah, I know. Looking back it's like a blur."
    ryan "So that's my story. Anything you'd like to learn more about?"

    # initialize all choices to False
    $ ryan_story_choices = [False, False, False, False]
    label ryan_story_choices:
        menu:
            "What are you up to nowadays?" if not ryan_story_choices[0]:
                mc "What are you up to nowadays?"
                ryan "If you are looking for a one-word answer, then it's “learning.” Everyone else I know will probably give you the same answer if you ask."
                $ ryan_story_choices[0] = True
                jump ryan_story_choices

            "Do you still have much to learn as a senior engineer?" if not ryan_story_choices[1]:
                mc "Do you still have much to learn as a senior engineer?"
                ryan "Of course! I still run into technologies that are novel to me in my day-to-day."
                $ ryan_story_choices[1] = True
                jump ryan_story_choices

            "What is your experience working with people who have a CS degree versus who don't?" if not ryan_story_choices[2]:
                mc "What is your experience working with people who have a CS degree versus who don't?"
                ryan "I'd say it's not too different. A CS degree may give you a headstart in your first year as a junior developer, but after then, it is up to you to learn, grow, and adapt continuously to new technology."
                $ ryan_story_choices[2] = True
                jump ryan_story_choices

            "Do you have a favorite side project?" if not ryan_story_choices[3]:
                mc "Do you have a favorite side project?"
                ryan "There is one I'm working on right now. Top secret. You will know when you see it."
                ryan "Like I said, I majored in design and music in college. Design and music are two things that get me up in the morning."
                ryan "Now that I've also learned to code, I think it's prime time to put my passion into use to create something awesome, like a video game. I get to do the art, music, and coding all by myself."
                mc "That sure sounds like fun! I'd love to see it one day!"
                $ ryan_story_choices[3] = True
                jump ryan_story_choices

            "I'm done asking!":
                mc "I'm done asking! That's all I want to know. Thanks so much for sharing!"
                ryan "Anytime, [persistent.player_name]. Have fun coding and keep me updated on your progress!"

label stage8_interviews:
    # Stage 8. Coding interviews
    scene bg bedroom night with dissolve
    mc "I read that technical jobs ask candidates to complete coding interviews."
    mc "I know how to code, so these interviews shouldn't be too hard if I study, right?"
    mc "Let's do this."
    mc "Hmm? What is a heap? I remember learning about lists and dictionaries in my course, but definitely not heaps."
    mc "And heaps are under data structure fundamentals. Does that mean that I need to learn to implement a heap from scratch?"
    mc "What is time complexity? What about space complexity? Does that mean that my code needs to run fast in addition to being correct?"
    mc "Coding interviews are so different from coding..."
    mc "Maybe I need to take some more courses specifically for coding interviews?"
    mc "So I've applied to over 30 jobs this week."
    mc "Submitted my resume, a cover letter, and whatnot."
    mc "Yet nothing has happened."
    mc "Let's maybe wait this out."
    mc "Is there something wrong with my application?"
    mc "I heard that some companies first screen resumes using AI, so maybe my resume never got to a recruiter..."
    mc "I know I don't have the strongest resume, but still..."
    mc "I've done what I could.I don't have a CS degree, so I took a quite comprehensive course. It is 300 hours! I even completed the end-of-curriculum project and put it on my GitHub."
    mc "Maybe they threw my resume away as soon as they saw that I'm not a CS major."
    mc "There is nothing I can do about that..."
    mc "I guess the best I can do is to apply to more companies."
    mc "That aside, in case I do hear back from anyone, what's next?"
    mc "I read that the next step is usually an online assessment that features LeetCode-style questions."
    mc "My coding interview skills are still pretty shaky. So let's keep grinding LeetCode while I wait."
    mc "Oh, an email!"
    mc "DevWire just sent me an online assessment!"
    mc "They said I have a week to complete it and must do it in a 90-minute sitting."
    mc "Well, here goes nothing."
    mc "How come I have no idea what these questions are trying to get at?"
    mc "They do look similar to some questions I saw on LeetCode, but I still have zero clue."

label stage14_becca:
    # Stage 14. New hire player
    scene bg office with dissolve
    show becca
    becca "Hey [persistent.player_name]. I'm Becca. I'm your onboarding buddy. Feel free to ask me anything."
    mc "Hi Becca. Nice to meet you."
    mc "... Um..."
    becca "Something on your mind?"
    mc "I'm kind of stuck... Or, I guess a more accurate way to put this is, I don't even know where to start."
    becca "No worries! Onboarding could be daunting."
    becca "Think about it. Teams of talented developers spent months, even years, building out this codebase."
    mc "Haha, thanks. That does make me feel better."
    becca "How about this? Let's take your mind off this code for a while and go grab coffee?"
    mc "Sure, I'd love to!"
    mc "Hey Becca. Mind if I ask how long you've been with this company and team?"
    becca "Of course not! I've been here for two years. I interned here when I was in college and returned full-time right after graduation."
    mc "So you were a CS major?"
    becca "Yep."
    becca "Oh please I know that look. CS kids must have had it the easy way."
    becca "That's not true, you know."
    mc "Oops, sorry."
    becca "No big deal."
    becca "Have you heard of the word, imposter syndrome?"
    mc "Yeah. I feel that quite often."
    becca "You are good. That's almost the norm for people in tech."
    becca "Hah. Would you believe me if I tell you that imposter syndrome hits CS students equally hard, if not harder?"
    mc "... Um... Tell me about it."
    becca "It starts the first time we step into a CS classroom, maybe earlier. There is always that kid that sits in the front row, who has been coding since five and knows everything the professor has yet to talk about."
    mc "That's... intense."
    becca "And there is the expectation that CS kids should get big-names internships as early as their freshman year summer. Definitely not later than their junior year summer. Otherwise, the myth goes that they are unhirable."
    becca "I spent my freshman and sophomore summers volunteering at a local school teaching kids to code. I don't see any problems with that. I mean, I love coding and I love teaching, and being able to convey that to the next generation is an awesome opportunity for me."
    becca "But my friends were either interning for big names or building their own startups during the summer. They are nice enough not to say anything to my face, but I always feel a strange sense of hollowness when I see them post about their intern perks or startup progress."
    becca "It was a rough time, but my friends and my college advisors were supportive, and I eventually come to terms with being who I am and contributing to causes that I care about."
    becca "Haha sorry for the rant. I didn't mean to scare you away from continuing working in tech."
    becca "It's just that the battle with imposter syndrome is a continuous battle. Every little win is a win. In fact, I still grapple with imposter syndrome and have to stop myself from banging my head on the desk whenever I run into a bug I can't fix."
    mc "Wow. Haha. Thanks for sharing. That actually makes me feel a lot better."
    becca "So are we ready to go back and squash some bugs?"
    mc "Lead the way!"

    return
