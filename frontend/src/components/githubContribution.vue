<template>
  <div class="container" v-show="datas">
    <div
      v-for="(weeks, weekIndex) in datas?.weeks"
      :key="weekIndex"
      class="weeks"
    >
      {{ weekIndex }}
      <div
        v-for="cell in weeks.contributionDays"
        :key="cell.firstDay"
        class="cell"
        :style="{ backgroundColor: cell.color }"
        :title="`${cell.contributionCount === 0 ? 'No contribution' : cell.contributionCount + ' contributions'} on ${cell.date}`"
      ></div>
    </div>
  </div>
</template>
<script setup>
import { shallowRef } from 'vue'
import { githubApiKey, githubName } from '/secret.js' // 从前端项目根目录 secret.js 中导入 githubApiKey
import { getGithubContributions } from '@/api/github.js'

let datas = shallowRef(null)

;(async () => {
  console.log('hello GithubContribution.vue')
  const { data } = await getGithubContributions(githubName, githubApiKey)
  datas.value = data.data.user.contributionsCollection.contributionCalendar
})()
</script>
<style scoped>
.container {
  display: flex;
  flex-direction: row;
  background-color: #fff;
}

.weeks {
  display: flex;
  flex-direction: column;
}

.cell {
  width: 16px;
  height: 16px;
  background-color: green;
  margin: 2px; /* Add some margin for better visualization */
}
</style>
