#!/usr/bin/env python3
"""
Enhanced Interview Preparation System
A comprehensive Python-based ML interview preparation tool
"""

import json
import random
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from collections import defaultdict
import os

@dataclass
class Question:
    """Represents an interview question"""
    id: int
    question: str
    answer: str
    category: str
    difficulty: str
    tags: List[str]
    
    def to_dict(self) -> Dict:
        return asdict(self)

class QuestionBank:
    """Manages the collection of interview questions"""
    
    def __init__(self):
        self.questions: List[Question] = []
        self._load_default_questions()
    
    def _load_default_questions(self):
        """Load default ML interview questions"""
        default_questions = [
            Question(
                id=1,
                question="What is the difference between supervised and unsupervised learning?",
                answer="Supervised learning uses labeled data to train models, while unsupervised learning finds patterns in unlabeled data. Supervised learning includes classification and regression tasks, while unsupervised includes clustering and dimensionality reduction.",
                category="ML",
                difficulty="Easy",
                tags=["supervised", "unsupervised", "learning", "fundamentals"]
            ),
            Question(
                id=2,
                question="Explain the concept of overfitting and how to prevent it.",
                answer="Overfitting occurs when a model learns the training data too well but fails to generalize to new data. Prevention methods include: regularization (L1/L2), cross-validation, early stopping, dropout, data augmentation, and using more training data.",
                category="ML",
                difficulty="Medium",
                tags=["overfitting", "regularization", "generalization", "validation"]
            ),
            Question(
                id=3,
                question="What is a convolutional neural network and when would you use it?",
                answer="A CNN is a neural network designed for processing grid-like data such as images. It uses convolutional layers to detect local features, pooling layers to reduce dimensionality, and is commonly used for image classification, object detection, and computer vision tasks.",
                category="DL",
                difficulty="Medium",
                tags=["cnn", "convolution", "image", "deep learning", "computer vision"]
            ),
            Question(
                id=4,
                question="How does transfer learning work in deep learning?",
                answer="Transfer learning involves using a pre-trained model on a new but related task. The model's learned features are transferred and fine-tuned for the new task, requiring less data and training time. Common approaches include feature extraction and fine-tuning.",
                category="DL",
                difficulty="Medium",
                tags=["transfer learning", "pre-trained", "fine-tuning", "feature extraction"]
            ),
            Question(
                id=5,
                question="What is the difference between classification and regression?",
                answer="Classification predicts discrete categories/classes (e.g., spam/not spam), while regression predicts continuous numerical values (e.g., house prices). Classification outputs probabilities or class labels, while regression outputs real numbers.",
                category="ML",
                difficulty="Easy",
                tags=["classification", "regression", "prediction", "supervised learning"]
            ),
            Question(
                id=6,
                question="Explain the concept of gradient descent and its variants.",
                answer="Gradient descent is an optimization algorithm that minimizes loss functions by iteratively moving in the direction of steepest descent. Variants include: SGD (stochastic), Mini-batch GD, Adam (adaptive moments), RMSprop, and AdaGrad.",
                category="DL",
                difficulty="Hard",
                tags=["gradient descent", "optimization", "adam", "sgd", "backpropagation"]
            ),
            Question(
                id=7,
                question="What is the attention mechanism in transformers?",
                answer="Attention allows the model to focus on different parts of the input sequence when making predictions. It computes attention weights to determine which input elements are most relevant. Self-attention enables the model to relate different positions in a sequence.",
                category="NLP",
                difficulty="Hard",
                tags=["attention", "transformer", "nlp", "sequence", "self-attention"]
            ),
            Question(
                id=8,
                question="How do you handle imbalanced datasets?",
                answer="Techniques include: resampling (SMOTE, undersampling), using different evaluation metrics (precision, recall, F1, AUC), adjusting class weights, ensemble methods, and threshold tuning. Choose based on the specific problem and dataset size.",
                category="ML",
                difficulty="Medium",
                tags=["imbalanced", "resampling", "evaluation", "smote", "class weights"]
            ),
            Question(
                id=9,
                question="What is the difference between precision and recall?",
                answer="Precision measures the accuracy of positive predictions (TP/(TP+FP)) - 'Of all positive predictions, how many were correct?'. Recall measures the ability to find all positive instances (TP/(TP+FN)) - 'Of all actual positives, how many did we find?'.",
                category="ML",
                difficulty="Medium",
                tags=["precision", "recall", "metrics", "evaluation", "confusion matrix"]
            ),
            Question(
                id=10,
                question="Explain the concept of batch normalization.",
                answer="Batch normalization normalizes the inputs of each layer by computing the mean and variance across the batch. It helps with training stability, faster convergence, allows higher learning rates, and acts as a form of regularization.",
                category="DL",
                difficulty="Hard",
                tags=["batch normalization", "training", "stability", "regularization"]
            ),
            Question(
                id=11,
                question="What is cross-validation and why is it important?",
                answer="Cross-validation is a technique to assess model performance by splitting data into multiple folds, training on some and testing on others. It provides better estimates of model performance, helps detect overfitting, and is crucial for model selection and hyperparameter tuning.",
                category="ML",
                difficulty="Medium",
                tags=["cross-validation", "model evaluation", "k-fold", "overfitting"]
            ),
            Question(
                id=12,
                question="Explain the bias-variance tradeoff.",
                answer="Bias is error from overly simplistic assumptions, variance is error from sensitivity to small fluctuations in training data. High bias leads to underfitting, high variance to overfitting. The goal is to find the sweet spot that minimizes total error (bias² + variance + noise).",
                category="ML",
                difficulty="Hard",
                tags=["bias", "variance", "tradeoff", "underfitting", "overfitting"]
            ),
            Question(
                id=13,
                question="What are RNNs and what problems do they solve?",
                answer="Recurrent Neural Networks process sequential data by maintaining hidden states that capture information from previous time steps. They solve problems involving sequences like language modeling, machine translation, and time series prediction. LSTMs and GRUs address vanishing gradient problems.",
                category="DL",
                difficulty="Medium",
                tags=["rnn", "lstm", "gru", "sequential", "time series", "nlp"]
            ),
            Question(
                id=14,
                question="How do you evaluate a machine learning model?",
                answer="Evaluation depends on the task: Classification (accuracy, precision, recall, F1, AUC-ROC), Regression (MSE, MAE, R²), and general techniques (cross-validation, train/val/test splits, learning curves). Always consider business metrics and model interpretability.",
                category="ML",
                difficulty="Medium",
                tags=["evaluation", "metrics", "accuracy", "mse", "auc", "cross-validation"]
            ),
            Question(
                id=15,
                question="What is the difference between bagging and boosting?",
                answer="Bagging (Bootstrap Aggregating) trains multiple models in parallel on different subsets of data and averages predictions (e.g., Random Forest). Boosting trains models sequentially, where each model corrects errors of previous ones (e.g., AdaBoost, XGBoost).",
                category="ML",
                difficulty="Hard",
                tags=["bagging", "boosting", "ensemble", "random forest", "xgboost", "adaboost"]
            )
        ]
        self.questions = default_questions
    
    def get_all_questions(self) -> List[Question]:
        """Get all questions"""
        return self.questions
    
    def filter_questions(self, category: Optional[str] = None, 
                        difficulty: Optional[str] = None,
                        search_term: Optional[str] = None) -> List[Question]:
        """Filter questions by category, difficulty, or search term"""
        filtered = self.questions
        
        if category:
            filtered = [q for q in filtered if q.category == category]
        
        if difficulty:
            filtered = [q for q in filtered if q.difficulty == difficulty]
        
        if search_term:
            search_term = search_term.lower()
            filtered = [q for q in filtered if 
                       search_term in q.question.lower() or 
                       search_term in q.answer.lower() or
                       any(search_term in tag.lower() for tag in q.tags)]
        
        return filtered
    
    def get_random_questions(self, count: int, categories: Optional[List[str]] = None) -> List[Question]:
        """Get random questions for mock interview"""
        available = self.questions
        if categories:
            available = [q for q in available if q.category in categories]
        
        return random.sample(available, min(count, len(available)))
    
    def add_question(self, question: Question):
        """Add a new question to the bank"""
        self.questions.append(question)
    
    def save_to_file(self, filename: str):
        """Save questions to JSON file"""
        with open(filename, 'w') as f:
            json.dump([q.to_dict() for q in self.questions], f, indent=2)
    
    def load_from_file(self, filename: str):
        """Load questions from JSON file"""
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                data = json.load(f)
                self.questions = [Question(**q) for q in data]

class MockInterview:
    """Handles mock interview sessions"""
    
    def __init__(self, question_bank: QuestionBank):
        self.question_bank = question_bank
        self.current_session = None
    
    def start_interview(self, num_questions: int = 10, 
                       time_limit: int = 30,
                       categories: Optional[List[str]] = None) -> Dict:
        """Start a new mock interview session"""
        questions = self.question_bank.get_random_questions(num_questions, categories)
        
        self.current_session = {
            'questions': questions,
            'current_index': 0,
            'start_time': datetime.now(),
            'time_limit': time_limit,  # in minutes
            'answers_shown': [],
            'completed': False
        }
        
        return {
            'total_questions': len(questions),
            'time_limit': time_limit,
            'categories': categories or ['All']
        }
    
    def get_current_question(self) -> Optional[Dict]:
        """Get the current question in the interview"""
        if not self.current_session or self.current_session['completed']:
            return None
        
        if self.current_session['current_index'] >= len(self.current_session['questions']):
            return None
        
        question = self.current_session['questions'][self.current_session['current_index']]
        elapsed_time = (datetime.now() - self.current_session['start_time']).total_seconds() / 60
        time_remaining = max(0, self.current_session['time_limit'] - elapsed_time)
        
        return {
            'question_number': self.current_session['current_index'] + 1,
            'total_questions': len(self.current_session['questions']),
            'question': question.question,
            'category': question.category,
            'difficulty': question.difficulty,
            'time_remaining': time_remaining,
            'answer': question.answer  # Hidden by default in UI
        }
    
    def next_question(self):
        """Move to the next question"""
        if self.current_session:
            self.current_session['current_index'] += 1
            if self.current_session['current_index'] >= len(self.current_session['questions']):
                self.current_session['completed'] = True
    
    def show_answer(self):
        """Mark that answer was shown for current question"""
        if self.current_session:
            current_idx = self.current_session['current_index']
            if current_idx not in self.current_session['answers_shown']:
                self.current_session['answers_shown'].append(current_idx)
    
    def get_results(self) -> Dict:
        """Get interview results"""
        if not self.current_session:
            return {}
        
        total_time = (datetime.now() - self.current_session['start_time']).total_seconds() / 60
        questions_answered = min(self.current_session['current_index'], 
                               len(self.current_session['questions']))
        
        # Calculate category distribution
        categories = defaultdict(int)
        difficulties = defaultdict(int)
        
        for i in range(questions_answered):
            question = self.current_session['questions'][i]
            categories[question.category] += 1
            difficulties[question.difficulty] += 1
        
        return {
            'questions_answered': questions_answered,
            'total_questions': len(self.current_session['questions']),
            'time_used': round(total_time, 1),
            'time_limit': self.current_session['time_limit'],
            'answers_shown': len(self.current_session['answers_shown']),
            'category_distribution': dict(categories),
            'difficulty_distribution': dict(difficulties),
            'completion_rate': round(questions_answered / len(self.current_session['questions']) * 100, 1)
        }

class ProgressTracker:
    """Tracks user progress and statistics"""
    
    def __init__(self, filename: str = "progress.json"):
        self.filename = filename
        self.data = self._load_progress()
    
    def _load_progress(self) -> Dict:
        """Load progress from file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {
            'total_questions_seen': 0,
            'total_interviews': 0,
            'total_study_time': 0,
            'category_progress': defaultdict(int),
            'difficulty_progress': defaultdict(int),
            'interview_history': []
        }
    
    def save_progress(self):
        """Save progress to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2, default=str)
    
    def update_interview_stats(self, results: Dict):
        """Update statistics after an interview"""
        self.data['total_interviews'] += 1
        self.data['total_questions_seen'] += results['questions_answered']
        self.data['total_study_time'] += results['time_used']
        
        # Update category and difficulty progress
        for category, count in results['category_distribution'].items():
            self.data['category_progress'][category] += count
        
        for difficulty, count in results['difficulty_distribution'].items():
            self.data['difficulty_progress'][difficulty] += count
        
        # Add to history
        self.data['interview_history'].append({
            'date': datetime.now().isoformat(),
            'results': results
        })
        
        self.save_progress()
    
    def get_statistics(self) -> Dict:
        """Get comprehensive statistics"""
        if self.data['total_questions_seen'] == 0:
            return {
                'total_questions': 0,
                'total_interviews': 0,
                'study_time_hours': 0,
                'average_completion_rate': 0,
                'category_breakdown': {},
                'difficulty_breakdown': {}
            }
        
        # Calculate average completion rate
        completion_rates = [h['results'].get('completion_rate', 0) 
                          for h in self.data['interview_history']]
        avg_completion = sum(completion_rates) / len(completion_rates) if completion_rates else 0
        
        return {
            'total_questions': self.data['total_questions_seen'],
            'total_interviews': self.data['total_interviews'],
            'study_time_hours': round(self.data['total_study_time'] / 60, 1),
            'average_completion_rate': round(avg_completion, 1),
            'category_breakdown': dict(self.data['category_progress']),
            'difficulty_breakdown': dict(self.data['difficulty_progress'])
        }

class StudyPlan:
    """Generates personalized study plans"""
    
    def __init__(self, progress_tracker: ProgressTracker):
        self.progress_tracker = progress_tracker
    
    def generate_plan(self, weeks: int = 4) -> Dict:
        """Generate a personalized study plan"""
        stats = self.progress_tracker.get_statistics()
        category_progress = stats['category_breakdown']
        
        # Define curriculum
        curriculum = {
            'Week 1': {
                'topic': 'Machine Learning Fundamentals',
                'focus': 'ML',
                'subtopics': [
                    'Linear Regression & Logistic Regression',
                    'Decision Trees & Random Forest',
                    'Support Vector Machines',
                    'Cross-validation techniques',
                    'Bias-Variance Tradeoff'
                ]
            },
            'Week 2': {
                'topic': 'Deep Learning',
                'focus': 'DL',
                'subtopics': [
                    'Neural Networks basics',
                    'Convolutional Neural Networks',
                    'Recurrent Neural Networks',
                    'Transfer Learning',
                    'Batch Normalization'
                ]
            },
            'Week 3': {
                'topic': 'Computer Vision',
                'focus': 'CV',
                'subtopics': [
                    'Image preprocessing',
                    'Object detection',
                    'Image segmentation',
                    'Feature extraction',
                    'CNN architectures'
                ]
            },
            'Week 4': {
                'topic': 'Natural Language Processing',
                'focus': 'NLP',
                'subtopics': [
                    'Text preprocessing',
                    'Word embeddings',
                    'Sequence models',
                    'Transformer architecture',
                    'Attention mechanisms'
                ]
            }
        }
        
        # Calculate progress for each week based on category performance
        for week, content in curriculum.items():
            focus_category = content['focus']
            total_questions = sum(category_progress.values()) if category_progress else 1
            category_questions = category_progress.get(focus_category, 0)
            progress_percentage = min(100, (category_questions / total_questions) * 100) if total_questions > 0 else 0
            content['progress'] = round(progress_percentage, 1)
        
        return curriculum
    
    def get_recommendations(self) -> List[str]:
        """Get personalized recommendations"""
        stats = self.progress_tracker.get_statistics()
        recommendations = []
        
        if stats['total_interviews'] == 0:
            recommendations.append("Start with a mock interview to assess your current level")
        
        if stats['average_completion_rate'] < 70:
            recommendations.append("Focus on time management - practice answering questions more quickly")
        
        # Find weakest category
        category_progress = stats['category_breakdown']
        if category_progress:
            weakest_category = min(category_progress.items(), key=lambda x: x[1])
            recommendations.append(f"Spend more time on {weakest_category[0]} questions")
        
        if stats['study_time_hours'] < 5:
            recommendations.append("Increase your study time - aim for at least 1 hour per day")
        
        return recommendations

class InterviewPrepSystem:
    """Main system that coordinates all components"""
    
    def __init__(self):
        self.question_bank = QuestionBank()
        self.mock_interview = MockInterview(self.question_bank)
        self.progress_tracker = ProgressTracker()
        self.study_plan = StudyPlan(self.progress_tracker)
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("🎓 ENHANCED INTERVIEW PREP SYSTEM")
        print("="*50)
        print("1. Browse Question Bank")
        print("2. Start Mock Interview")
        print("3. View Progress")
        print("4. Study Plan")
        print("5. Add Custom Question")
        print("6. Export/Import Questions")
        print("0. Exit")
        print("="*50)
    
    def browse_questions(self):
        """Browse and filter questions"""
        print("\n📚 QUESTION BANK")
        print("-" * 30)
        
        # Get filter preferences
        print("Filter options (press Enter to skip):")
        category = input("Category (ML/DL/CV/NLP): ").upper() or None
        difficulty = input("Difficulty (Easy/Medium/Hard): ").title() or None
        search_term = input("Search term: ") or None
        
        questions = self.question_bank.filter_questions(category, difficulty, search_term)
        
        if not questions:
            print("No questions found matching your criteria.")
            return
        
        print(f"\nFound {len(questions)} questions:")
        print("-" * 50)
        
        for i, q in enumerate(questions, 1):
            print(f"\n{i}. [{q.category}] [{q.difficulty}] {q.question}")
            show_answer = input("Show answer? (y/n): ").lower() == 'y'
            if show_answer:
                print(f"💡 Answer: {q.answer}")
                print(f"🏷️  Tags: {', '.join(q.tags)}")
            
            if i < len(questions):
                continue_browse = input("\nContinue to next question? (y/n): ").lower() == 'y'
                if not continue_browse:
                    break
    
    def start_mock_interview(self):
        """Start a mock interview session"""
        print("\n🎯 MOCK INTERVIEW SETUP")
        print("-" * 30)
        
        try:
            num_questions = int(input("Number of questions (5-20): ") or "10")
            time_limit = int(input("Time limit in minutes (15-60): ") or "30")
            
            print("Select categories (comma-separated, or press Enter for all):")
            print("Available: ML, DL, CV, NLP")
            categories_input = input("Categories: ").upper()
            categories = [c.strip() for c in categories_input.split(",")] if categories_input else None
            
            # Start interview
            session_info = self.mock_interview.start_interview(num_questions, time_limit, categories)
            print(f"\n🚀 Starting interview with {session_info['total_questions']} questions")
            print(f"⏰ Time limit: {session_info['time_limit']} minutes")
            
            # Interview loop
            while True:
                current_q = self.mock_interview.get_current_question()
                if not current_q:
                    break
                
                print(f"\n{'='*60}")
                print(f"Question {current_q['question_number']}/{current_q['total_questions']}")
                print(f"Category: {current_q['category']} | Difficulty: {current_q['difficulty']}")
                print(f"Time remaining: {current_q['time_remaining']:.1f} minutes")
                print(f"{'='*60}")
                print(f"\n❓ {current_q['question']}")
                
                print("\nOptions:")
                print("1. Show answer")
                print("2. Next question")
                print("3. End interview")
                
                choice = input("\nYour choice (1-3): ")
                
                if choice == "1":
                    self.mock_interview.show_answer()
                    print(f"\n💡 Answer: {current_q['answer']}")
                    input("\nPress Enter to continue...")
                elif choice == "2":
                    self.mock_interview.next_question()
                elif choice == "3":
                    break
                else:
                    print("Invalid choice. Moving to next question.")
                    self.mock_interview.next_question()
            
            # Show results
            results = self.mock_interview.get_results()
            self.display_interview_results(results)
            
            # Update progress
            self.progress_tracker.update_interview_stats(results)
            
        except ValueError:
            print("Invalid input. Please enter numbers where required.")
    
    def display_interview_results(self, results: Dict):
        """Display interview results"""
        print("\n" + "="*50)
        print("🏆 INTERVIEW RESULTS")
        print("="*50)
        print(f"Questions Answered: {results['questions_answered']}/{results['total_questions']}")
        print(f"Completion Rate: {results['completion_rate']:.1f}%")
        print(f"Time Used: {results['time_used']:.1f}/{results['time_limit']} minutes")
        print(f"Answers Shown: {results['answers_shown']}")
        
        print(f"\n📊 Category Distribution:")
        for category, count in results['category_distribution'].items():
            print(f"  {category}: {count} questions")
        
        print(f"\n📈 Difficulty Distribution:")
        for difficulty, count in results['difficulty_distribution'].items():
            print(f"  {difficulty}: {count} questions")
    
    def view_progress(self):
        """Display progress statistics"""
        stats = self.progress_tracker.get_statistics()
        
        print("\n" + "="*50)
        print("📊 YOUR PROGRESS")
        print("="*50)
        print(f"Total Questions Practiced: {stats['total_questions']}")
        print(f"Total Interviews: {stats['total_interviews']}")
        print(f"Study Time: {stats['study_time_hours']} hours")
        print(f"Average Completion Rate: {stats['average_completion_rate']:.1f}%")
        
        if stats['category_breakdown']:
            print(f"\n📚 Category Breakdown:")
            for category, count in stats['category_breakdown'].items():
                print(f"  {category}: {count} questions")
        
        if stats['difficulty_breakdown']:
            print(f"\n🎯 Difficulty Breakdown:")
            for difficulty, count in stats['difficulty_breakdown'].items():
                print(f"  {difficulty}: {count} questions")
    
    def show_study_plan(self):
        """Display personalized study plan"""
        plan = self.study_plan.generate_plan()
        recommendations = self.study_plan.get_recommendations()
        
        print("\n" + "="*50)
        print("📅 PERSONALIZED STUDY PLAN")
        print("="*50)
        
        for week, content in plan.items():
            print(f"\n{week}: {content['topic']}")
            print(f"Progress: {content['progress']:.1f}%")
            print("Topics to cover:")
            for subtopic in content['subtopics']:
                print(f"  • {subtopic}")
        
        if recommendations:
            print(f"\n💡 RECOMMENDATIONS:")
            for rec in recommendations:
                print(f"  • {rec}")
    
    def add_custom_question(self):
        """Add a custom question"""
        print("\n➕ ADD CUSTOM QUESTION")
        print("-" * 30)
        
        try:
            question_text = input("Question: ")
            answer_text = input("Answer: ")
            category = input("Category (ML/DL/CV/NLP): ").upper()
            difficulty = input("Difficulty (Easy/Medium/Hard): ").title()
            tags_input = input("Tags (comma-separated): ")
            tags = [tag.strip() for tag in tags_input.split(",")]
            
            new_id = max([q.id for q in self.question_bank.questions]) + 1
            new_question = Question(
                id=new_id,
                question=question_text,
                answer=answer_text,
                category=category,
                difficulty=difficulty,
                tags=tags
            )
            
            self.question_bank.add_question(new_question)
            print("✅ Question added successfully!")
            
        except Exception as e:
            print(f"Error adding question: {e}")
    
    def export_import_questions(self):
        """Export or import questions"""
        print("\n💾 EXPORT/IMPORT QUESTIONS")
        print("-" * 30)
        print("1. Export questions to file")
        print("2. Import questions from file")
        
        choice = input("Your choice (1-2): ")
        
        if choice == "1":
            filename = input("Export filename (default: questions.json): ") or "questions.json"
            self.question_bank.save_to_file(filename)
            print(f"✅ Questions exported to {filename}")
        elif choice == "2":
            filename = input("Import filename: ")
            if os.path.exists(filename):
                self.question_bank.load_from_file(filename)
                print(f"✅ Questions imported from {filename}")
            else:
                print("❌ File not found")
    
    def run(self):
        """Main application loop"""
        print("Welcome to Enhanced Interview Prep System!")
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (0-6): ")
            
            if choice == "0":
                print("Thank you for using Interview Prep System! Good luck! 🍀")
                break
            elif choice == "1":
                self.browse_questions()
            elif choice == "2":
                self.start_mock_interview()
            elif choice == "3":
                self.view_progress()
            elif choice == "4":
                self.show_study_plan()
            elif choice == "5":
                self.add_custom_question()
            elif choice == "6":
                self.export_import_questions()
            else:
                print("Invalid choice. Please try again.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    # Create and run the interview prep system
    system = InterviewPrepSystem()
    system.run()