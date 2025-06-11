import pandas as pd
import numpy as np



def map_job_to_category(job_title):
    if not isinstance(job_title, str):
        return None # Handle non-string values like NaN

    # Standardize job title for robust matching
    title_lower = job_title.lower()

    # --- Priority 1: Highly specific and clear matches ---

    # HEALTHCARE
    if any(keyword in title_lower for keyword in ['nurse', 'physician', 'therapist', 'medical', 'dental hygienist', 'veterinarian', 'pediatrician']):
        return 'HEALTHCARE'

    # ADVOCATE (Legal)
    if any(keyword in title_lower for keyword in ['attorney', 'lawyer', 'legal counsel', 'legal advisor', 'paralegal', 'legal assistant', 'legal secretary']):
        return 'ADVOCATE'

    # ACCOUNTANT
    if 'accountant' in title_lower:
        return 'ACCOUNTANT'

    # TEACHER
    if 'teacher' in title_lower:
        return 'TEACHER'

    # PUBLIC-RELATIONS
    if 'public relations' in title_lower:
        return 'PUBLIC-RELATIONS'

    # DIGITAL-MEDIA (Includes marketing, SEO, content)
    if any(keyword in title_lower for keyword in ['marketing', 'social media', 'seo', 'sem', 'copywriter', 'content writer', 'digital media']):
        return 'DIGITAL-MEDIA'

    # HR
    if any(keyword in title_lower for keyword in ['hr', 'human resources']):
        return 'HR'

    # BANKING (Specific finance roles)
    if 'investment banker' in title_lower or 'banking' in title_lower:
        return 'BANKING'

    # AVIATION (Specific engineering within Aviation)
    if 'aerospace engineer' in title_lower:
        return 'AVIATION'

    # --- Priority 2: Broader categories with overlaps ---

    # INFORMATION-TECHNOLOGY
    # Check for specific IT roles before general 'engineer'
    if any(keyword in title_lower for keyword in [
        'software', 'developer', 'web developer', 'ui developer', 'backend', 'frontend',
        'data scientist', 'data engineer', 'data analyst', 'research analyst',
        'network', 'database', 'systems administrator', 'it support', 'it manager',
        'qa analyst', 'qa engineer', 'software tester', 'cybersecurity',
        'business analyst', 'computer scientist', 'technical writer' # Technical writer often falls under IT
    ]):
        # Exclude general engineering types that should go to 'ENGINEERING'
        if not any(k in title_lower for k in ['mechanical', 'civil', 'electrical', 'chemical', 'structural', 'process', 'environmental', 'landscape', 'architectural']):
            return 'INFORMATION-TECHNOLOGY'

    # ENGINEERING (Non-IT specific, including environmental engineering)
    if any(keyword in title_lower for keyword in [
        'engineer', 'mechanical', 'civil', 'electrical', 'chemical', 'structural', 'process',
        'environmental' # Environmental engineer maps here, and then to AGRICULTURE-ENVIRONMENT via the function
    ]):
        # Catch specific design engineers that should go to DESIGN-CREATIVE
        if not any(k in title_lower for k in ['designer', 'architectural', 'landscape']):
            return 'ENGINEERING'

    # DESIGN-CREATIVE (Now includes broader "Arts" aspects too)
    if any(keyword in title_lower for keyword in [
        'designer', 'ux', 'ui', 'graphic', 'web designer', 'art director', 'interior', 'landscape architect', 'architectural designer', 'product designer'
    ]):
        return 'DESIGN-CREATIVE'

    # SALES
    if any(keyword in title_lower for keyword in ['sales', 'account manager', 'account director', 'account executive', 'brand ambassador', 'customer success manager', 'customer service manager', 'customer service representative', 'customer support specialist']):
        return 'SALES' # Merging customer service into sales for simplicity, as they are often related

    # FINANCE
    if any(keyword in title_lower for keyword in ['financial', 'investment', 'finance manager', 'controller', 'tax consultant']):
        return 'FINANCE'

    # OPERATIONS-ADMIN (Includes Project Management, Supply Chain, Admin, BPO-like roles)
    if any(keyword in title_lower for keyword in [
        'operations', 'project manager', 'project coordinator', 'procurement', 'supply chain',
        'inventory', 'office manager', 'administrative assistant', 'personal assistant', 'executive assistant',
        'event manager', 'event planner', 'event coordinator', 'wedding planner' # Event roles can fit here
    ]):
        return 'OPERATIONS-ADMIN'

    # CONSTRUCTION (Includes architecture and urban planning)
    if any(keyword in title_lower for keyword in ['architect', 'construction', 'urban planner']):
        return 'CONSTRUCTION'

    # BUSINESS-DEVELOPMENT
    if 'business development' in title_lower:
        return 'BUSINESS-DEVELOPMENT'


    # AGRICULTURE-ENVIRONMENT (Catch environmental if not specifically an engineer)
    if 'environmental' in title_lower:
        return 'AGRICULTURE-ENVIRONMENT'

    return 'UNCATEGORIZED' # If no clear match is found




def map_job_to_category_modified(job_title):
    if not isinstance(job_title, str):
        return None
    title_lower = job_title.lower()

    # --- IMPORTANT: New order and updated logic for AGRICULTURE-ENVIRONMENT ---

    # AGRICULTURE-ENVIRONMENT (New highest priority for all environmental and agriculture roles)
    if any(keyword in title_lower for keyword in [
        'environmental', 'agriculture', 'agronomist', 'horticulturist',
        'farm manager', 'ecologist', 'conservationist', 'forestry', 'sustainability manager' # Broadened keywords
    ]):
        return 'AGRICULTURE-ENVIRONMENT'

    # --- Other specific categories (mostly unchanged order) ---

    # HEALTHCARE
    if any(keyword in title_lower for keyword in ['nurse', 'physician', 'therapist', 'medical', 'dental hygienist', 'veterinarian', 'pediatrician', 'substance abuse counselor', 'social worker', 'psychologist']):
        return 'HEALTHCARE'
    # ADVOCATE (Legal)
    if any(keyword in title_lower for keyword in ['attorney', 'lawyer', 'legal counsel', 'legal advisor', 'paralegal', 'legal assistant', 'legal secretary']):
        return 'ADVOCATE'
    # ACCOUNTANT
    if 'accountant' in title_lower:
        return 'ACCOUNTANT'
    # TEACHER
    if 'teacher' in title_lower:
        return 'TEACHER'
    # PUBLIC-RELATIONS
    if 'public relations' in title_lower:
        return 'PUBLIC-RELATIONS'
    # DIGITAL-MEDIA
    if any(keyword in title_lower for keyword in ['marketing', 'social media', 'seo', 'sem', 'copywriter', 'content writer', 'digital media', 'brand manager', 'market analyst', 'market research analyst']):
        return 'DIGITAL-MEDIA'
    # HR
    if any(keyword in title_lower for keyword in ['hr', 'human resources']):
        return 'HR'
    # BANKING
    if 'investment banker' in title_lower or 'banking' in title_lower:
        return 'BANKING'
    # AVIATION
    if 'aerospace engineer' in title_lower:
        return 'AVIATION'

    # INFORMATION-TECHNOLOGY (Includes SAP Specialist)
    if any(keyword in title_lower for keyword in [
        'software', 'developer', 'web developer', 'ui developer', 'backend', 'frontend',
        'data scientist', 'data engineer', 'data analyst', 'research analyst',
        'network', 'database', 'systems administrator', 'it support', 'it manager', 'it administrator',
        'qa analyst', 'qa engineer', 'software tester', 'quality assurance analyst',
        'systems analyst', 'cybersecurity', 'business analyst', 'computer scientist', 'technical writer',
        'sap specialist', 'sap consultant', 'sap analyst'
    ]):
        if not any(k in title_lower for k in [
            'mechanical engineer', 'civil engineer', 'electrical engineer', 'chemical engineer',
            'structural engineer', 'process engineer', # Removed 'environmental' from here
            'scientist',
            'landscape architect', 'architectural designer'
        ]):
            return 'INFORMATION-TECHNOLOGY'

    # ENGINEERING-SCIENCE (Removed 'environmental' keyword here as it's now caught by AGRICULTURE-ENVIRONMENT)
    if any(keyword in title_lower for keyword in [
        'engineer', 'mechanical', 'civil', 'electrical', 'chemical', 'structural', 'process',
        'research scientist', 'scientist'
    ]):
        if not any(k in title_lower for k in ['designer', 'architectural designer', 'landscape architect']):
            return 'ENGINEERING-SCIENCE'

    # DESIGN-CREATIVE
    if any(keyword in title_lower for keyword in [
        'designer', 'ux', 'ui', 'graphic', 'web designer', 'art director', 'interior', 'landscape architect', 'architectural designer', 'product designer'
    ]):
        return 'DESIGN-CREATIVE'

    # SALES
    if any(keyword in title_lower for keyword in ['sales', 'account manager', 'account director', 'account executive', 'brand ambassador', 'customer success manager', 'customer service manager', 'customer service representative', 'customer support specialist']):
        return 'SALES'

    # FINANCE
    if any(keyword in title_lower for keyword in ['financial', 'investment', 'finance manager', 'controller', 'tax consultant']):
        return 'FINANCE'

    # OPERATIONS-ADMIN (Now also catches generic 'consultant' roles, but lower priority than specific 'environmental')
    if any(keyword in title_lower for keyword in [
        'operations', 'project manager', 'project coordinator', 'procurement', 'supply chain',
        'inventory', 'office manager', 'administrative assistant', 'personal assistant', 'executive assistant',
        'event manager', 'event planner', 'event coordinator', 'wedding planner',
        'purchasing agent', 'data entry clerk', 'product manager',
        'consultant' # Generic consultant goes here
    ]):
        # Ensure it's not a more specific consultant type already caught above
        if not any(k in title_lower for k in [
            'marketing consultant', 'digital marketing consultant', 'financial consultant',
            'tax consultant', 'it consultant', 'tech consultant', 'sap consultant',
            'healthcare consultant', 'hr consultant', 'engineering consultant', 'scientific consultant'
        ]): # Removed 'environmental consultant' as it's now caught by AGRICULTURE-ENVIRONMENT
            return 'OPERATIONS-ADMIN'

    # CONSTRUCTION
    if any(keyword in title_lower for keyword in ['architect', 'construction', 'urban planner']):
        return 'CONSTRUCTION'

    # BUSINESS-DEVELOPMENT
    if 'business development' in title_lower:
        return 'BUSINESS-DEVELOPMENT'

    return 'UNCATEGORIZED' # Default if no clear match is found

