
# DTI 412 - Lab 3-4
# Part 4: QuerySet API, Advanced Logic and Optimization

from django.db.models import Q
import django.db
from core.models import Employee, Course

# Task 4.1: Q Objects
query_or = Employee.objects.filter(
    Q(department__code="IT") | Q(salary__gt=70000)
)
print("OR Query Results:", list(query_or))

query_not = Employee.objects.filter(
    Q(first_name__icontains="John") & ~Q(department__code="HR")
)
print("AND NOT Query Results:", list(query_not))

# Task 4.2: F Expressions
# Already executed successfully. Do not run again.
# Employee.objects.filter(department__code="IT").update(
#     salary=F('salary') * 1.10
# )

# Task 4.3: Unoptimized Query
django.db.reset_queries()
employees = Employee.objects.all()

for emp in employees:
    print(f"Employee: {emp.first_name}, Department: {emp.department.name}")

print("Unoptimized Queries:",
      len(django.db.connection.queries))

# Task 4.3: select_related()
django.db.reset_queries()
optimized_employees = Employee.objects.select_related('department').all()

for emp in optimized_employees:
    print(f"Employee: {emp.first_name}, Department: {emp.department.name}")

print("select_related Queries:",
      len(django.db.connection.queries))

# Task 4.4: prefetch_related()
django.db.reset_queries()
courses = Course.objects.prefetch_related('attendees').all()

for course in courses:
    attendee_names = [
        emp.first_name for emp in course.attendees.all()
    ]
    print(f"Course: {course.code}, Attendees: {', '.join(attendee_names)}")

print("prefetch_related Queries:",
      len(django.db.connection.queries))

