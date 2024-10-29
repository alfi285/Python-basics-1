#Write a Python program to check if a person qualifies
# for a discount based on their age, membership status,
# and whether they have a referral code.

#Use and to check if the person is at least 18 years old
# and has a valid membership.
#Use not to ensure the person does not have an expired membership.
#Use or to add an alternative condition that will
# pass if the person has a valid referral code,
# even if they don’t meet the age requirement.
#If any of these conditions are met,
# print "Discount Applied!", otherwise print "No Discount".

age = 19
is_membership = True
is_membership_expired = True
referalcode = False

if age>= 18 and (is_membership==True and not is_membership_expired==True) or referalcode==True:
    print("Discount applied")
else:
    print("Not applied")

#(age >= 18 and has_membership and not membership_expired):
#This checks if the individual is at least 18 years old,
# has a membership, and that the membership is not expired.
# All three conditions must be true
# for this part of the condition to evaluate to True.


#or has_referral_code:
#This checks if the individual has a referral code.
# If this condition is true,
# the overall condition will be true regardless of the previous part.
