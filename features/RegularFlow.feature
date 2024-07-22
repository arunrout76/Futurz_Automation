Feature: Regular Flow Feature.

  Scenario: Login as Admin
    Given Reschedule the Batch from Username as "arun01" and Password as "Arun@420" and batch is "74ba43ee-30a1-43d3-86c4-f50756f9b65f"
    When The batch has been rescheduled for Now
    Then Rescheduled Successfully

  Scenario: Login as Instructor then start and End Session
    Given Reschedule the Batch from Instructor Username as "aruninstructor5" and Password as "Aruninstructor@65868"
    When Start the Session
    Then Take Attendance

  Scenario: Login as User then start and End Session
    Given Reschedule the Batch from Student Username as "lahey" and Password as "Lahey@63259"
    When Workouts are Completed
    Then Feedback is Given