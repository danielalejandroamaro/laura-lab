<script setup>
import WelcomeItem from "./WelcomeItem.vue";
import DocumentationIcon from "./icons/IconDocumentation.vue";
import ToolingIcon from "./icons/IconTooling.vue";
import EcosystemIcon from "./icons/IconEcosystem.vue";
import CommunityIcon from "./icons/IconCommunity.vue";
import SupportIcon from "./icons/IconSupport.vue";
import Persona from "./persona.vue";
</script>

<script>
import axios from "axios";

export default {
  name: "theWelcome",
  data() {
    return {
      personas: [],
      newName: "",
      newSex: "M",
      sexOptions: ["M", "F", "B"],
    };
  },
  beforeMount() {
    axios
      .get("http://localhost:8000/nombres")
      .then((res) => res.data)
      .then((personas) => {
        this.personas = personas;
      });
  },
  methods: {
    createItem() {},
    removeItem(name) {
      let index = this.personas.findIndex((x) => x.name == name);
      alert("removing " + name + " " + index);
      if (index > -1) {
        console.log(
          "http://localhost:8000/nombres/" + this.personas[index]["id"]
        );
        axios
          .delete("http://localhost:8000/nombres/" + this.personas[index]["id"])
          .then(() => {
            this.personas.splice(index, 1);
          });
      }
    },
    insertInto() {
      axios
        .post("http://localhost:8000/nombres/", {
          name: this.newName,
          sex: this.newSex,
        })
        .then((res) => res.data)
        .then((new_persona) => {
          this.personas.push(new_persona);
        });
    },
  },
};
</script>


<template>
  <div>
    <h1>Hola</h1>
    <div>
      <label for="sex">Sexo</label>
      <select key="sex" v-model="newSex">
        <option v-for="sexOption in sexOptions" :key="sexOption">
          {{ sexOption }}
        </option>
      </select>
      <label for="name"> insert a new name</label>
      <input type="text" key="name" v-model="newName" />
      <button @click="insertInto">insert</button>
    </div>
    <ul>
      <persona
        :persona="persona"
        v-for="persona in personas"
        @removeItem="removeItem"
      />
    </ul>
    <p>{{ names }}</p>
    <p>{{ newName }}</p>
  </div>
</template>


