FROM archlinux/base:latest
WORKDIR  /app
COPY requirements.txt .
RUN  pacman -Syu --noconfirm && pacman -S python python-pip --noconfirm &&  pip install -r requirements.txt
COPY . .
RUN echo "PYTHONPATH=/usr/lib/python3.7" >> ~/.bashrc
CMD source ~/.bashrc
CMD ["python","server.py"]
