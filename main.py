#!/usr/bin/env python3

import argparse
from simple_qa import simple_qa

def main():
    parser = argparse.ArgumentParser(description="Run different DSPy prompts")
    parser.add_argument("mode", choices=["basic"], help="The mode to run")
    parser.add_argument("question", help="The question to ask")
    
    args = parser.parse_args()
    
    try: 
        if args.mode == "basic":
            answer = simple_qa(args.question)
            print(f"Answer: {answer}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()