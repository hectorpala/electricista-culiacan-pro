#!/usr/bin/env python3
"""
Automated deployment script with pre-deployment checks
Electricista Culiacán Pro - Deploy Automation
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list, description: str) -> bool:
    """Run a command and return success status"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Success")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - Failed")
        print(e.stderr)
        return False


def check_git_status() -> bool:
    """Check if there are uncommitted changes"""
    print("\n🔍 Checking git status...")
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)

    if result.stdout.strip():
        print("⚠️  Uncommitted changes detected:")
        print(result.stdout)
        return False
    else:
        print("✅ No uncommitted changes")
        return True


def validate_sitemap() -> bool:
    """Validate sitemap.xml"""
    print("\n🗺️  Validating sitemap.xml...")
    sitemap = Path("sitemap.xml")

    if not sitemap.exists():
        print("❌ sitemap.xml not found")
        return False

    # Use xmllint to validate
    try:
        subprocess.run(
            ["xmllint", "--noout", "--schema",
             "https://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd",
             "sitemap.xml"],
            check=True,
            capture_output=True
        )
        print("✅ sitemap.xml is valid")
        return True
    except subprocess.CalledProcessError:
        print("❌ sitemap.xml validation failed")
        return False
    except FileNotFoundError:
        print("⚠️  xmllint not found, skipping validation")
        return True


def check_cname() -> bool:
    """Check CNAME file"""
    print("\n🌐 Checking CNAME...")
    cname = Path("CNAME")

    if not cname.exists():
        print("❌ CNAME file not found")
        return False

    with open(cname, "r") as f:
        domain = f.read().strip()

    if domain != "electricistaculiacanpro.mx":
        print(f"❌ CNAME contains wrong domain: {domain}")
        return False

    print(f"✅ CNAME is correct: {domain}")
    return True


def run_pre_deployment_checks() -> bool:
    """Run all pre-deployment checks"""
    print("\n" + "=" * 60)
    print("🚀 Pre-Deployment Checks")
    print("=" * 60)

    checks = [
        ("Git Status", check_git_status),
        ("Sitemap Validation", validate_sitemap),
        ("CNAME Check", check_cname),
    ]

    all_passed = True
    for name, check_func in checks:
        if not check_func():
            all_passed = False
            print(f"❌ {name} failed")

    return all_passed


def deploy():
    """Execute deployment"""
    print("\n" + "=" * 60)
    print("🚀 Deploying to GitHub Pages")
    print("=" * 60)

    # Run pre-deployment checks
    if not run_pre_deployment_checks():
        print("\n❌ Pre-deployment checks failed. Aborting deployment.")
        sys.exit(1)

    # Git push
    if not run_command(["git", "push", "origin", "main"], "Pushing to GitHub"):
        print("\n❌ Deployment failed during git push")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("✅ Deployment Complete!")
    print("=" * 60)
    print("\n🌐 Your site will be available at:")
    print("   https://electricistaculiacanpro.mx")
    print("\n⏱️  Note: It may take 1-2 minutes for changes to appear")
    print("=" * 60)


def main():
    """Main execution"""
    print("🚀 Electricista Culiacán Pro - Deployment Script")

    # Check if we're in the right directory
    if not Path(".git").exists():
        print("❌ Not a git repository. Run this from the project root.")
        sys.exit(1)

    # Run deployment
    deploy()


if __name__ == "__main__":
    main()
