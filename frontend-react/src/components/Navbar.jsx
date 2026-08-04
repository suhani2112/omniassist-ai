function Navbar() {
  return (
    <header className="flex h-16 items-center justify-between border-b border-gray-800 bg-gray-900 px-6">
      {/* Left */}
      <div>
        <h1 className="text-2xl font-bold text-white">
          🤖 OmniAssistAI
        </h1>

        <p className="text-sm text-gray-400">
          AI Assistant with Memory & RAG
        </p>
      </div>

      {/* Right */}
      <div className="flex items-center gap-3">
        <div className="rounded-full bg-green-500 px-3 py-1 text-sm font-medium text-white">
          ● Online
        </div>
      </div>
    </header>
  );
}

export default Navbar;