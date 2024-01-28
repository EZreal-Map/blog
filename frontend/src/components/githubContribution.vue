<template>
  <div class="container" v-show="datas">
    <div
      v-for="(weeks, weekIndex) in datas?.weeks"
      :key="weekIndex"
      class="weeks"
    >
      <div v-for="cell in weeks.contributionDays" :key="cell.firstDay">
        <el-tooltip
          class="box-item"
          effect="dark"
          :content="`${cell.contributionCount === 0 ? 'No contribution' : cell.contributionCount + ' contributions'} on ${cell.date}`"
          placement="top"
        >
          <div class="cell" :style="{ backgroundColor: cell.color }"></div>
        </el-tooltip>
      </div>
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
  console.log(datas.value)
})()
</script>
<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  background-color: #fff;
}

.weeks {
  display: flex;
  flex-direction: column;
}

.cell {
  width: 16px;
  height: 18px;
  margin: 2px; /* Add some margin for better visualization */
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1);
}
.cell:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style>
