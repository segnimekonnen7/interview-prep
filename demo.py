#!/usr/bin/env python3
"""
Demo script for Enhanced Interview Prep System
Shows how to use the system programmatically
"""

from interview_prep import (
    InterviewPrepSystem, 
    QuestionBank, 
    MockInterview, 
    ProgressTracker,
    StudyPlan,
    Question
)

def demo_question_bank():
    """Demonstrate QuestionBank functionality"""
    print("🔍 QUESTION BANK DEMO")
    print("=" * 40)
    
    bank = QuestionBank()
    
    # Show total questions
    print(f"Total questions: {len(bank.get_all_questions())}")
    
    # Filter by category
    ml_questions = bank.filter_questions(category="ML")
    print(f"ML questions: {len(ml_questions)}")
    
    # Filter by difficulty
    hard_questions = bank.filter_questions(difficulty="Hard")
    print(f"Hard questions: {len(hard_questions)}")
    
    # Search functionality
    gradient_questions = bank.filter_questions(search_term="gradient")
    print(f"Questions about 'gradient': {len(gradient_questions)}")
    
    # Show first question
    if ml_questions:
        q = ml_questions[0]
        print(f"\nSample ML Question:")
        print(f"Q: {q.question}")
        print(f"A: {q.answer[:100]}...")
        print(f"Tags: {', '.join(q.tags)}")

def demo_mock_interview():
    """Demonstrate MockInterview functionality"""
    print("\n🎯 MOCK INTERVIEW DEMO")
    print("=" * 40)
    
    bank = QuestionBank()
    interview = MockInterview(bank)
    
    # Start a mock interview
    session_info = interview.start_interview(
        num_questions=3, 
        time_limit=5,  # 5 minutes for demo
        categories=["ML", "DL"]
    )
    
    print(f"Started interview with {session_info['total_questions']} questions")
    print(f"Categories: {session_info['categories']}")
    
    # Simulate going through questions
    question_count = 0
    while question_count < 3:
        current_q = interview.get_current_question()
        if not current_q:
            break
            
        print(f"\nQuestion {current_q['question_number']}: {current_q['question']}")
        print(f"Category: {current_q['category']} | Difficulty: {current_q['difficulty']}")
        print(f"Time remaining: {current_q['time_remaining']:.1f} minutes")
        
        # Simulate showing answer for first question
        if question_count == 0:
            interview.show_answer()
            print("✓ Answer shown")
        
        interview.next_question()
        question_count += 1
    
    # Get results
    results = interview.get_results()
    print(f"\n📊 Results:")
    print(f"Completion rate: {results['completion_rate']}%")
    print(f"Time used: {results['time_used']:.1f} minutes")
    print(f"Answers shown: {results['answers_shown']}")

def demo_progress_tracking():
    """Demonstrate ProgressTracker functionality"""
    print("\n📈 PROGRESS TRACKING DEMO")
    print("=" * 40)
    
    # Create a temporary progress tracker
    tracker = ProgressTracker("demo_progress.json")
    
    # Simulate some interview results
    sample_results = {
        'questions_answered': 8,
        'total_questions': 10,
        'time_used': 25.5,
        'time_limit': 30,
        'answers_shown': 2,
        'category_distribution': {'ML': 5, 'DL': 3},
        'difficulty_distribution': {'Easy': 3, 'Medium': 4, 'Hard': 1},
        'completion_rate': 80.0
    }
    
    # Update stats
    tracker.update_interview_stats(sample_results)
    
    # Get statistics
    stats = tracker.get_statistics()
    print(f"Total questions practiced: {stats['total_questions']}")
    print(f"Total interviews: {stats['total_interviews']}")
    print(f"Study time: {stats['study_time_hours']} hours")
    print(f"Average completion rate: {stats['average_completion_rate']}%")
    print(f"Category breakdown: {stats['category_breakdown']}")

def demo_study_plan():
    """Demonstrate StudyPlan functionality"""
    print("\n📚 STUDY PLAN DEMO")
    print("=" * 40)
    
    # Create tracker with some data
    tracker = ProgressTracker("demo_progress.json")
    study_plan = StudyPlan(tracker)
    
    # Generate plan
    plan = study_plan.generate_plan()
    
    for week, content in plan.items():
        print(f"\n{week}: {content['topic']}")
        print(f"Progress: {content['progress']}%")
        print("Key topics:")
        for topic in content['subtopics'][:3]:  # Show first 3
            print(f"  • {topic}")
    
    # Get recommendations
    recommendations = study_plan.get_recommendations()
    print(f"\n💡 Recommendations:")
    for rec in recommendations:
        print(f"  • {rec}")

def demo_custom_question():
    """Demonstrate adding custom questions"""
    print("\n➕ CUSTOM QUESTION DEMO")
    print("=" * 40)
    
    bank = QuestionBank()
    original_count = len(bank.get_all_questions())
    
    # Add a custom question
    custom_question = Question(
        id=100,
        question="What is the difference between L1 and L2 regularization?",
        answer="L1 regularization adds the sum of absolute values of parameters to the loss function, promoting sparsity. L2 regularization adds the sum of squared parameters, promoting smaller weights. L1 can lead to feature selection, while L2 prevents overfitting by shrinking weights.",
        category="ML",
        difficulty="Medium",
        tags=["regularization", "l1", "l2", "overfitting", "feature selection"]
    )
    
    bank.add_question(custom_question)
    new_count = len(bank.get_all_questions())
    
    print(f"Questions before: {original_count}")
    print(f"Questions after: {new_count}")
    print("✅ Custom question added successfully!")

def main():
    """Run all demos"""
    print("🎓 ENHANCED INTERVIEW PREP SYSTEM - DEMO")
    print("=" * 50)
    
    demo_question_bank()
    demo_mock_interview()
    demo_progress_tracking()
    demo_study_plan()
    demo_custom_question()
    
    print("\n" + "=" * 50)
    print("🚀 DEMO COMPLETED!")
    print("Run 'python interview_prep.py' to start the interactive system")
    print("=" * 50)
    
    # Clean up demo files
    import os
    if os.path.exists("demo_progress.json"):
        os.remove("demo_progress.json")
        print("🧹 Demo files cleaned up")

if __name__ == "__main__":
    main()