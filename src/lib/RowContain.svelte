<script>
  import LetterRow from "./LetterRow.svelte";
    
  export let guesses
</script>

{#each guesses as word}
  <LetterRow {word} test={true}/>
{/each}