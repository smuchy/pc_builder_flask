from py2neo import Graph, Node, Relationship
from passlib.hash import bcrypt
from flask import session
from datetime import datetime
from flask import jsonify
import os
import uuid

graph = Graph("bolt://localhost:7687", auth=("neo4j", "test"))


class User:
    def __init__(self, username):
        self.username = username

    def find(self):
        user = graph.run(
            "MATCH (user:User { username: '%s'} ) RETURN user" % self.username
        ).data()
        return user

    def findCpu(self, cpu):
        cpu = graph.run("MATCH (cpu:CPU { name: '%s'} ) RETURN cpu" % cpu).data()
        return cpu

    def findMotherboard(self, motherboard):
        motherboard = graph.run(
            "MATCH (motherboard:Motherboard { name: '%s'} ) RETURN motherboard"
            % motherboard
        ).data()
        return motherboard

    def findRam(self, ram):
        ram = graph.run("MATCH (ram:RAM { name: '%s'} ) RETURN ram" % ram).data()
        return ram

    def findStorage(self, storage):
        storage = graph.run(
            "MATCH (storage:Storage { name: '%s'} ) RETURN storage" % storage
        ).data()
        return storage

    def findVideoCard(self, video_card):
        video_card = graph.run(
            "MATCH (video_card:VideoCard { name: '%s'} ) RETURN video_card" % video_card
        ).data()
        return video_card

    def findCpuCooler(self, cpu_cooler):
        cpu_cooler = graph.run(
            "MATCH (cpu_cooler:CPUCooler { name: '%s'} ) RETURN cpu_cooler" % cpu_cooler
        ).data()
        return cpu_cooler

    def findCase(self, case):
        case = graph.run("MATCH (case:Case { name: '%s'} ) RETURN case" % case).data()
        return case

    def findPowerSupply(self, power_supply):
        power_supply = graph.run(
            "MATCH (power_supply:PowerSupply { name: '%s'} ) RETURN power_supply"
            % power_supply
        ).data()
        return power_supply

    def findOperatingSystem(self, operating_system):
        operating_system = graph.run(
            "MATCH (operating_system:OperatingSystem { name: '%s'} ) RETURN operating_system"
            % operating_system
        ).data()
        return operating_system

    def register(self, password, first_name, last_name, email):
        if not self.find():
            user = Node(
                "User",
                username=self.username,
                password=bcrypt.encrypt(password),
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            graph.create(user)
            return True
        else:
            return False

    def verify_password(self, password):
        user = self.find()
        if user:
            return bcrypt.verify(password, user[0]["user"]["password"])
        else:
            return False

    def serve_motherboards(self, cpu):
        motherboardList = graph.run(
            "MATCH (motherboard:Motherboard)-[:COMPATIBLE]->(cpu:CPU {name: '%s'}) return motherboard"
            % cpu
        ).data()
        return motherboardList

    def serve_rams(self):
        ramList = graph.run("MATCH (ram:RAM) RETURN ram").data()
        return ramList

    def serve_storages(self):
        storageList = graph.run("MATCH (storage:Storage) RETURN storage").data()
        return storageList

    def serve_video_cards(self):
        video_cardList = graph.run(
            "MATCH (video_card:Video Card) RETURN video_card"
        ).data()
        return video_cardList

    def serve_cpu_coolers(self):
        cpu_coolerList = graph.run(
            "MATCH (cpu_cooler:CPU Cooler) RETURN cpu_cooler"
        ).data()
        return cpu_coolerList

    def serve_cases(self):
        caseList = graph.run("MATCH (case:Case) RETURN case").data()
        return caseList

    def serve_power_supplies(self):
        power_supplyList = graph.run(
            "MATCH (power_supply:Power Supply) RETURN power_supply"
        ).data()
        return power_supplyList

    def serve_operating_systems(self):
        operating_systemList = graph.run(
            "MATCH (operating_system:Operating System) RETURN operating_system"
        ).data()
        return operating_systemList

    def add_pcbuild(
        self,
        cpu,
        motherboard,
        ram,
        storage,
        video_card,
        cpu_cooler,
        case,
        power_supply,
        operating_system,
    ):
        user = self.find()
        buildID = str(uuid.uuid4())
        build = Node(
            "Build",
            id=buildID,
            cpu=self.findCpu(cpu)[0]["cpu"]["name"],
            motherboard=self.findMotherboard(motherboard)[0]["motherboard"]["name"],
            ram=self.findRam(ram)[0]["ram"]["name"],
            storage=self.findStorage(storage)[0]["storage"]["name"],
            video_card=self.findVideoCard(video_card)[0]["video_card"]["name"],
            cpu_cooler=self.findCpuCooler(cpu_cooler)[0]["cpu_cooler"]["name"],
            case=self.findCase(case)[0]["case"]["name"],
            power_supply=self.findPowerSupply(power_supply)[0]["power_supply"]["name"],
            operating_system=self.findOperatingSystem(operating_system)[0][
                "operating_system"
            ]["name"],
        )
        graph.create(build)

        graph.run(
            "MATCH (user:User),(build: Build) where user.username = '%(username)s' and build.id = '%(buildID)s' create (user)-[r:BUILT]->(build)"
            % {"username": user[0]["user"]["username"], "buildID": buildID}
        )

        return jsonify(response="success")


def serve_cpus():
    return graph.run("MATCH (cpu:CPU) RETURN cpu").data()
