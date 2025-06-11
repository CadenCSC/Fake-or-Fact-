import os
import subprocess
from pycodestyle import StyleGuide

def check_and_fix_pep8(filepath):
    """
    Check a Python file for PEP 8 compliance and attempt to fix issues automatically.
    
    Args:
        filepath (str): Path to the Python file to check.
    """
    # Verify file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return
    
    print(f"Checking PEP 8 compliance for: {filepath}")
    print("-" * 50)
    
    # First check with pycodestyle
    print("\nRunning PEP 8 check...")
    style_guide = StyleGuide()
    result = style_guide.check_files([filepath])
    total_errors = result.total_errors
    print(f"Found {total_errors} PEP 8 violations")
    
    if total_errors > 0:
        # Try to automatically fix issues
        print("\nAttempting to automatically fix issues...")
        try:
            # Install autopep8 if not already installed
            subprocess.run(['pip', 'install', 'autopep8'], check=True)
            
            # Run autopep8 to fix issues
            subprocess.run([
                'autopep8',
                '--in-place',
                '--aggressive',
                '--max-line-length=79',
                filepath
            ], check=True)
            print("Automated fixes applied.")
            
            # Check again after fixes
            print("\nRunning PEP 8 check after fixes...")
            style_guide = StyleGuide()
            result = style_guide.check_files([filepath])
            remaining_errors = result.total_errors
            print(f"Remaining PEP 8 violations after fixes: {remaining_errors}")
            
        except subprocess.CalledProcessError as e:
            print(f"Error running autopep8: {e}")
        except Exception as e:
            print(f"Error: {e}")
    
    print("\nManual fixes needed for:")
    print("- Lines that are still too long (E501)")
    print("- Complex formatting issues")
    print("- Logical changes (like '== False' to 'is False')")

if __name__ == "__main__":
    # Path to your file - update this to your actual path
    file_to_check = r"C:\Users\caden\Desktop\CSC\Fake-or-Fact-\Fake or Fact.py"
    
    # Run the check and fix
    check_and_fix_pep8(file_to_check)
    
    print("\nDone! Check your file for remaining issues.")