# Запуск QuestDB
FROM questdb/questdb

# Для Debian/Ubuntu используйте следующую строку вместо предыдущей
RUN apt-get update && apt-get install -y curl

# Запуск QuestDB
#CMD ["questdb", "start"]
CMD ["/docker-entrypoint.sh", "start"]
#CMD ["sh", "-c", "/usr/local/bin/questdb.sh start && tail -f /dev/null"]
#CMD ["sh", "-c", "/usr/local/bin/questdb start"]
#CMD ["questdb.sh", "start"]
#CMD ["sh", "-c", "/usr/local/bin/questdb start"]
#CMD ["exec", "/app/bin/java", "-m", "io.questdb/io.questdb.ServerMain", "-d", "/root/.questdb"]
#CMD ["sh", "-c", "/usr/local/bin/gosu start"]