import smtplib
server = smtplib.SMTP('localhost')
server.sendmail("soothsayer@exapmle.org", "jcaesar@example.org",
                """To:jcaesar@example.org
                From:soothsayer@example.org
                
                Beware the Ides of March.
                """)
server.quit()
